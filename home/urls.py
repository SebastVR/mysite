from django.urls import path
from home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView.as_view()),
]