from django.urls import path


from .forms import ContactForm1, ContactForm2
from .views import ContactWizard

app_name = "tools"
urlpatterns = [
    path("contact/", ContactWizard.as_view([ContactForm1, ContactForm2])),
]
