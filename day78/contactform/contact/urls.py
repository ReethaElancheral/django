from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact-form/", views.contact_form, name="contact_form"),
    path("manual-contact-form/", views.manual_contact_form, name="manual_contact_form"),
]
