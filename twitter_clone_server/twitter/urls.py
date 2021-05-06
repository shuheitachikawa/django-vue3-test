from django.urls import path
from . import views

app_name = 'twitter'
urlpatterns = [
    path('', views.TweetListCreateAPIView.as_view()),
    path('<pk>', views.TweetRetrieveUpdateDestroyAPIView.as_view()),
]