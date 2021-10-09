from django.urls import path
from dimar import views


app_name = "dimar"
urlpatterns = [
    path("authors", views.manage_authors, name="manage_authors"),
    path("books", views.manage_books, name="manage_books"),
]
