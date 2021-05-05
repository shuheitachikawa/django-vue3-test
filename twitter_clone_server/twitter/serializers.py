from rest_framework import serializers
from .models import Tweet, Like

class TweetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tweet
    fields = ("__all__")

class LikeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Like
    fields = ("__all__")