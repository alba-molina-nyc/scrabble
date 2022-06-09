from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]










"""to create a urlconf in the directory you are in create a file called urls.py"""