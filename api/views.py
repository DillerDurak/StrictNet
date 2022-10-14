from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view

from main.models import Message, User
from .serializers import MessageSerializer


# class AddMessage(APIView):
#     def post(self, request):
#         data = request.data
#         sender = User.objects.get(id=request.user.id)
#         reciever = User.objects.get(id=)
#         message = MessageSerializer(data=request.data)
#         if message.is_valid():
#             message.save()
        
#         return Response(message.data)


@api_view(['POST'])
def add_message(request):
    data = request.data
    message = data['message']
    source = User.objects.get(username=data['source'])
    target = User.objects.get(username=data['target'])


    m = Message.objects.create(message=message,
                        sourceId=source,
                        targetId=target)

    return m

    
