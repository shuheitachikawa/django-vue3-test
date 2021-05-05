from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Tweet, Like
from .serializers import TweetSerializer, LikeSerializer

class TweetListAPIView(generics.ListAPIView):
  queryset = Tweet.objects.all()
  serializer_class = TweetSerializer

class LikeListAPIView(generics.ListAPIView):
  queryset = Like.objects.all()
  serializer_class = LikeSerializer