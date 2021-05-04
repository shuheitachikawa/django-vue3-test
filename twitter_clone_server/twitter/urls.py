from django.urls import path
from . import views

app_name = 'twitter'
urlpatterns = [
    path('', views.TwitterListAPIView.as_view(), name="index"),
]