from django.urls import path
from contact.views import *

app_name = "contact"
urlpatterns = [
    path("", contact_page , name="contact"),
]