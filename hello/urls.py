# from django.urls import path
# from hello import views

# urlpatterns = [
# path("", views.helloworld),
# path("", views.myview),
# ]

""" from django.urls import path
from hello import views

urlpatterns = [
    path("", views.helloworld),
] """

from django.urls import path
from hello import views
from django.views.generic import TemplateView

# app_name = "polls"

urlpatterns = [
    path("cookie", views.cookie),
    path("", views.sessfun),
]
