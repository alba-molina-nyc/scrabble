from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game', views.game, name='game'),
]










"""to create a urlconf in the directory you are in create a file called urls.py"""