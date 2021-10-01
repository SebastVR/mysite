from django.urls import path
from costs import views


app_name = "costs"
urlpatterns = [
    path("name", views.get_name, name="get_name"),
    path("cont", views.get_cont, name="get_cont"),
    path("cont_for", views.get_cont_for, name="get_cont_for"),
]
