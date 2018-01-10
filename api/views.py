from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import ContactSerializer
from .models import Contact
# Create your views here.

def home(request):
    return render(request, 'index.html', {})

class ContactView(APIView):
    serializer_class = ContactSerializer

    def get(self, request):
        serializer = self.serializer_class(Contact.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
