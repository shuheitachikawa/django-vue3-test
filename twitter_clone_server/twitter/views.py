from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import generics, views, status
from rest_framework.response import Response
from .models import Tweet, Like
from .serializers import TweetSerializer, LikeSerializer
from twitter import serializers

# class TweetListAPIView(generics.ListAPIView):
#   queryset = Tweet.objects.all()
#   serializer_class = TweetSerializer


class TweetListCreateAPIView(views.APIView):
  def get(self, request, *args, **kwargs):
    tweet_list = Tweet.objects.all().order_by('-created_at')
    serializer = TweetSerializer(instance=tweet_list, many=True)
    return Response(serializer.data, status.HTTP_200_OK)

  def post(self, request, *args, **kwargs):
    # acceptWord = 'test'
    # if (request.data['content'] != acceptWord):
    #   return Response('違います', status.HTTP_400_BAD_REQUEST)
    serializer = TweetSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status.HTTP_201_CREATED)

class TweetRetrieveUpdateDestroyAPIView(views.APIView):
  def get(self, request, pk, *args, **kwargs):
    tweet = get_object_or_404(Tweet, pk = pk)
    serializer = TweetSerializer(instance=tweet)
    return Response(serializer.data, status.HTTP_200_OK)

  def put(self, request, pk, *args, **kwargs):
    tweet = get_object_or_404(Tweet, pk = pk)
    serializer = TweetSerializer(instance=tweet, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status.HTTP_200_OK)

  def patch(self, request, pk, *args, **kwargs):
    tweet = get_object_or_404(Tweet, pk = pk)
    serializer = TweetSerializer(instance=tweet, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status.HTTP_200_OK)
  
  def delete(self, request, pk, *args, **kwargs):
    tweet = get_object_or_404(Tweet, pk = pk)
    tweet.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)






class LikeListAPIView(generics.ListAPIView):
  queryset = Like.objects.all()
  serializer_class = LikeSerializer