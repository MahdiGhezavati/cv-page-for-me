from django.urls import path
from info.views import *

app_name = "information"
urlpatterns = [
    path("",info , name="information"),
]