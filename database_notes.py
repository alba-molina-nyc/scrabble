"""
STEP 1 
open the terminal and type the command: 

createdb name_of_db_you_are_creating

STEP 2
go to settings in your main app, in this case scrabble
navigate to the DATABASES var that is holding a dictionary and make the appropriate changes

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqllite',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

to 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'scrabble'),
    }
}


"""