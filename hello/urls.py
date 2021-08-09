# from django.urls import path
# from hello import views

# urlpatterns = [
# path("", views.helloworld),
# path("", views.myview),
# ]

from django.urls import path
from hello import views

urlpatterns = [
    path("", views.helloworld),
]
