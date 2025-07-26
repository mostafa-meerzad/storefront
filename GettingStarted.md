## Create and Setup you Django Project

### 1 Create a Folder

Create a folder and name your project e.x: `storefront`.

### 2 Install Django

Go inside the folder and install django `pipenv install django` now pipenv installs django and crates `Pipfile` and `Pipfile.lock` which is the same file as `package.json` for javascript.

### 3 Activate the Virtual Environment

Now that the Django is installed we need to activate this virtual-environment so we can use the python interpreter in this virtual-environment not the one installed globally on our computer

to do so run `pipenv shell` in the terminal

now it's activated.

### 4 Use Django Admin

Now we need to use `django-admin` to start a new project. `django-admin` is a utility that comes with django.

`django-admin` provides these commands:

- compilemessages
- createcachetable
- dbshell
- diffsettings
- dumpdata
- flush
- inspectdb
- loaddata
- makemessages
- makemigrations
- migrate
- optimizemigration
- runserver
- sendtestemail
- shell
- showmigrations
- sqlflush
- sqlmigrate
- sqlsequencereset
- squashmigrations
- startapp
- startproject
- test
- testserver

but to start the project we use `django-admin startproject projectname`.

in our case: `django-admin startproject storefront`

this command crates a `storefront` inside it creates another directory `storefront` which is the core of our application. but we have redundancy!

to solve ti we need to run `django-admin startproject storefront .` the dot at the end means use current directory as the root of our project.

#### Inside project directory

- `__init__.py` which defines the directory as a package
- `settings.py` where we define our application settings
- `urls.py` where we define our application URLs
- and some others that are used for deployment

#### manage.py file

When we run `django-admin startproject` it also crated this `manage.py` file in the root of our application, which is a wrapper around django-admin, going forward instead of `django-admin` we use `manage.py` because `manage.py` takes the setting of the projects into account.

for example:

if we run `django-admin runserver` it's gonna throw an error saying `settings are not configured`

but if we run `python manage.py runserver` it's gonna start a dev server on default port "8000", we can optionally supply the port number.

##### Note

`python manage.py` command returns the same commands as `django-admin`

## Crating Your First App

Every Django project is essentially a collection of various apps, each providing a certain functionality, just like our mobile phones with many apps each one providing a certain functionality.

in our `settings.py` file we have:

```py
INSTALLED_APPS = [
    'django.contrib.admin', # which gives us admin interface for managing our data
    'django.contrib.auth', # used for authenticating users
    'django.contrib.contenttypes', # well get to this later
    'django.contrib.sessions', # this app is legacy and not used that much these days, so safe to delete
    'django.contrib.messages', # used for displaying one time notifications to the user
    'django.contrib.staticfiles', # used for serving static files like images, css and etc.
]

```

which is a list of installed apps on our project.

to create our own app run `python manage.py startapp appName` we use `python manage.py startapp playground`.

the command above crates a `playground` directory in the root of our project.

**Note**: every Django app has the exact same structure

```txt
playground
- migrations    # we'll get to this later
- admin.py  # where we define how the admin interface for this app will look like
- apps.py  # where we configure this app "the name is misleading"
- models.py  # where we define model classes to pull out data from database and present it to the user
- tests.py  # where we write our tests
- views.py  # where we handle requests and responses
```

every time you crate a new app, yo need to register it in the `settings.py` file `INSTALLED_APPS`

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "playground"
]
```
