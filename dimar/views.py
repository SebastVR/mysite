from django.forms import modelformset_factory
from django.shortcuts import render
from .models import Author, Book


def manage_authors(request):
    AuthorFormSet = modelformset_factory(Author, fields=("name", "title"))
    if request.method == "POST":
        formset = AuthorFormSet(
            request.POST,
            request.FILES,
            queryset=Author.objects.filter(name__startswith="O"),
        )
        if formset.is_valid():
            formset.save()
            # Do something.
    else:
        formset = AuthorFormSet(queryset=Author.objects.filter(name__startswith="O"))
    return render(request, "manage_authors.html", {"formset": formset})


def manage_books(request):
    BookFormSet = modelformset_factory(Book, fields=("name", "authors"))
    if request.method == "POST":
        formset = BookFormSet(
            request.POST,
            request.FILES,
            queryset=Book.objects.filter(name__startswith="O"),
        )
        if formset.is_valid():
            formset.save()
            # Do something.
    else:
        formset = BookFormSet(queryset=Book.objects.filter(name__startswith="O"))
    return render(request, "manage_authors.html", {"formset": formset})
