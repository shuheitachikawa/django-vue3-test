from django.urls import path
from . import views

app_name = 'twitter'
urlpatterns = [
    path('', views.TweetListAPIView.as_view(), name="index"),
]