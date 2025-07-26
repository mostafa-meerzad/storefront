from django.urls import path
from . import views

# make a special variable

# this is called a URLConf "url configuration"
urlpatterns = [
  path("hello/", views.say_hello)
]