"""
when you want to create your first "view" 

STEP 1. 

create a file called urls.py 
- then create a variable that will hold a list of all the views you want on there
- make sure you are importing at the top all the necessary items in order for your code to work from whatever modules you are importing from or depending from in order to get the urls

urlpatterns = [
    path('', views.index, name='index'),
]

when you want to add more views you will come back to the urlpatterns variable for the list and them on there based on the logic written above
"""
"""
from django.urls import URLPattern, path
from . import views


path is a function used for routing urls to the appropriate view functions within a django app, it uses the url dispatcher 
urlpatterns = [
    path_function(args, args, name_args)
    path('', views.index, name='index'),
]


path() argument: view¶
When Django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first argument and any “captured” values from the route as keyword arguments. We’ll give an example of this in a bit.

path() argument: kwargs¶
Arbitrary keyword arguments can be passed in a dictionary to the target view. We aren’t going to use this feature of Django in the tutorial.


path() argument: name¶
Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.

When you’re comfortable with the basic request and response flow, read part 2 of this tutorial to start working with the database.
"""



"""
STEP 2. 
then go to views. py
write a function that will return that view
things to keep in mind: make sure you are importing from django all the necessary items to make the import at the top 
for ex: 
    for an http view (the most simplest of views) you will need to import HttpResponse at the top
    then you will write in the function and you will be returning the HttpResponse you will be using in the function

def index(request):
    return HttpResponse("hi")
"""

"""
STEP 3
then you need to go to your main django server, in this case it is scrabble 
go to urls.py in there
and make sure in scrabble/urls.py you add the name of this new app that you have added to your django application inside the variable urlpatterns that holds a list of all the urls for all the apps you will be adding to your django application

--------
the include function we wrote in at the top allows referencing other urlconfs, whenever django encounters include() it chops off whatever part of the URL matched up to that point and sends the remaining string to the included urlconf for future processing

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('word_board.urls')),
    path('admin/', admin.site.urls),
]

so if you add any more apps to this django application for example, if you add some users app, this is where you will add it in order to see those urls for that app

make sure you follow this format
"""

"""
STEP 4
go to settings.py
and under 
the variable that holds a list of the installed apps called: 

INSTALLED APPS = []

add the app you just created, in this case: word_board, like this:

INSTALLED_APPS = [
    'word_board',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

"""