from rest_framework import serializers
from .models import Twitter

class TwitterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Twitter
    fields = ('id')