from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import user_serializer
from rest_framework import permissions
def index(request):
    return render(request, 'detail.html');

class API_prototype(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class = user_serializer
