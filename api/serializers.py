from rest_framework import serializers
from main.models import Message

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['sourceId', 'targetId', 'message']
    
   