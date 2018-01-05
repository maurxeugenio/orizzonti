from .models import Contact
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        depth = 0
        fields = ['id', 'name', 'subject', 'message', 'email']
