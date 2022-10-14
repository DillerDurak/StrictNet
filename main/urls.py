from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('sign-up/', views.RegisterUser.as_view(), name='registration'),
    path('logout/', views.logout_user, name='logout'),
    path('messages/', views.message_list, name='message_list'),
    path('messages/<int:id>/', views.message, name='message'),
]