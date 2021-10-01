from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
from .forms import NameForm, ContForm, Cont_for_Form


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        print("mostar1:", form)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print("mostrar algo ", form.is_valid())
            return HttpResponseRedirect("/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        print("mostrar2:", form)

    return render(request, "name.html", {"form": form})

    # return render(request, "name.html", {"form": form, "current_name": "Ariza"})


def get_cont(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ContForm(request.POST)
        print("mostar1:", form)
        # check whether it's valid:

        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["sender"]
            cc_myself = form.cleaned_data["cc_myself"]

            recipients = ["info@example.com"]
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect("/")
    else:
        form = ContForm()
        print("mostrar2:", form)

    return render(request, "cont.html", {"form": form})


def get_cont_for(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = Cont_for_Form(request.POST)
        print("mostar1:", form)
        # check whether it's valid:

        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["sender"]
            cc_myself = form.cleaned_data["cc_myself"]

            recipients = ["info@example.com"]
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect("/")
    else:
        form = Cont_for_Form()
        print("mostrar2:", form)

    return render(request, "cont_for.html", {"form": form})
