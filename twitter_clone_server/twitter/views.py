from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Twitter
from .serializers import TwitterSerializer

class TwitterListAPIView(generics.ListAPIView):
  queryset = Twitter.objects.all()
  serializer_class = TwitterSerializer