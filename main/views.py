from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.db.models import Q
import logging

from .forms import MessageForm, MyUserCreationForm, LoginForm
from .models import *


logger = logging.getLogger('main')


def index(request):
    logger.info('main page')
    return render(request, 'index.html', {})


class RegisterUser(CreateView):
    form_class = MyUserCreationForm
    template_name = 'register.html'

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return redirect('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def message_list(request):
    id = request.user.id
    users = User.objects.filter(message__targetId=id).order_by('username').distinct('username')
    # print(users)
    # messages = user.message.filter(sourceId=id)
    # messages = Message.objects.filter(Q(sourceId=id) | Q(targetId=id))
    

    context = {'users': users}

    return render(request, 'main/message_list.html', context)


def message(request, id):
    messages = Message.objects.filter(Q(sourceId=request.user.id, targetId=id)|Q(sourceId=id, targetId=request.user.id))
    sourceId = User.objects.get(id=request.user.id)
    targetId = User.objects.get(id=id)
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            m = Message.objects.create(
                sourceId=sourceId,
                targetId=targetId,
                message=message
            )
            logger.info(f'{sourceId.username} - {targetId.username}: {m.message}')
    
    code_str = chr(100+sourceId.id*targetId.id) if sourceId.id*targetId.id < 70 else chr(100+sourceId.id*targetId.id%70)
    code = str(sourceId.id*targetId.id) + code_str
    
    context = {'messages': messages, 'user': targetId, 'code': code, 'form':form}



    return render(request, 'main/chat.html', context)

