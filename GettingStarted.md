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

## Views

### ✅ What are Views in Django?

**Views** in Django are **Python functions or classes** that handle **incoming HTTP requests** and return **HTTP responses** (like HTML, JSON, etc).

You can think of views as the **"brains"** of your app. They take in a request, process data (often from the database), and decide what to return.

---

### 🧠 Example Breakdown

```python
# views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Mostafa!")
```

This view:

- Accepts a request (`home(request)`)
- Returns an HTTP response (just a plain string for now)

---

### 🛤 How Views Fit in the Flow

1. **User visits** a URL in their browser
2. Django checks the `urls.py` to match the URL to a view
3. That **view function runs**, maybe fetching data from the database
4. The view **returns a response**, often using a template

---

### 🏗 Types of Views

- **Function-Based Views (FBV)** → simpler, what you're using now
- **Class-Based Views (CBV)** → more powerful, reusable, and customizable (you'll learn these later)

---

here is our first view:

```py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def say_hello(request):
    return HttpResponse("Hello World")

```

now we need to map this view to a url, so when we get a request to that url this function will be called.

## Mapping URLs to View

Let's say whenever we send a request to `http://127.0.0.1:8000/playground/hello` our view function should be called and return `Hello World` to the user.

1. in your app folder `playground` in our case. crate a `urls.py` file, here we map our URLs to our View functions.

```py
from django.urls import path
from . import views

# make a special variable, all lowercase "urlpatterns"

# this is called a URLConf "url configuration"
urlpatterns = [
    # use the path function to crate a url-pattern object "path(route, view)"
  path("playground/hello/", views.say_hello)
]
```

now this file is a url-configuration module, then we need to import this urlConfig to our main urlConfig module `storefront` the core of our django application.

2. in the main `urls.py` file, first we need to import `include` function as there is comments for it. then add the path for your view.

`path("app_name/", include("app_name.urls"))`, in our case `path("playground/", include("playground.urls"))`

---

### playground app url

```py
from django.urls import path
from . import views

# make a special variable
# this is called a URLConf "url configuration"
urlpatterns = [
  path("playground/hello/", views.say_hello)
]
```

### main urls

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("playground/", include("playground.urls"))
]
```

with our **playground** urlConf in our main urls file we can remove the `playground` from the beginning of the views in our **playground** app. because django knows that urls starting with `playground` is handled by `playground.urls`, it chops off the first part of urls like this "playground/hello" to "hello" and this is passed to the view functions of playground app.

```py
from django.urls import path
from . import views

# make a special variable

# this is called a URLConf "url configuration"
urlpatterns = [
  path("hello/", views.say_hello)
]
```

---

in other words

Perfect! Now you're moving into **URL routing**, which is what tells Django **"when a user visits this URL, run this view."**

Let’s break it down with a clear step-by-step example 👇

---

### ✅ Step-by-Step: Mapping Views to URLs

#### 1. **Create a View**

In your app's `views.py`:

```python
# views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my Django app, Mostafa!")
```

---

#### 2. **Create a URL pattern in your app**

In your app folder (e.g., `myapp/urls.py`), create this file if it doesn’t exist:

```python
# myapp/urls.py
from django.urls import path
from . import views  # Import your views file

urlpatterns = [
    path('', views.home, name='home'),  # '' = root of the app
]
```

---

#### 3. **Include your app's URLs in the main project**

In your **project's** main `urls.py` (usually in a folder named same as the project):

```python
# project_name/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # include app’s urls
]
```

This means:

- When someone visits `http://localhost:8000/`, Django looks at `myapp/urls.py`
- Then it runs the `home()` view because `''` matches the root

---

### 📌 Bonus: Add More Views

```python
# views.py
def about(request):
    return HttpResponse("This is the About page.")
```

```python
# myapp/urls.py
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

Now:

- `/` → Home page
- `/about/` → About page

---

## Using Templates

to use templates first crate `templates` directory inside your app
then put your `html` files there "a template is just a HTML file that is rendered on a request"

to render the template when user hits an endpoint we need to render it as follows:

```py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def say_hello(request):
     return render(request, "hello.html")

```

we can also pass some data to our templates `render(request, "hello.html", {"name": "mostafa"})` the third argument takes a dictionary and it's keys are accessible in the template inside `{{}}` double curly braces `<h1>Hello {{name}}</h1>`

---

in other words

Great question, Mostafa — and good on you for being curious even if the course is moving past templates. Let’s break it all down.

---

### 🎨 What Are Django Templates?

Django templates are **HTML files** that can contain **special template tags** and **variables**.

They're rendered by views to dynamically show data — like showing a list of products, user names, messages, etc.

---

### 🧠 Basic View-to-Template Flow

```python
# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'name': 'Mostafa'})
```

- `'home.html'` is the template file
- `{'name': 'Mostafa'}` is the context dictionary (data passed to template)

---

### 🗂 Folder Structure

Django expects templates to be inside a folder named `templates`.

Example:

```
myapp/
├── templates/
│   └── home.html
├── views.py
```

Or if you want to share templates across multiple apps:

```
project_root/
├── templates/
│   └── home.html
```

Then in your **`settings.py`**, make sure `DIRS` is set:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Enable global template folder
        ...
    },
]
```

---

### 🧾 Example Template: `home.html`

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Django Site</title>
  </head>
  <body>
    <h1>Hello, {{ name }}!</h1>
  </body>
</html>
```

Here:

- `{{ name }}` will be replaced with `"Mostafa"` from the context.

---

### ➕ Passing More Data

```python
def about(request):
    context = {
        'developer': 'Mostafa Meerzad',
        'skills': ['Python', 'Django', 'React']
    }
    return render(request, 'about.html', context)
```

```html
<!-- about.html -->
<h2>{{ developer }}</h2>
<ul>
  {% for skill in skills %}
  <li>{{ skill }}</li>
  {% endfor %}
</ul>
```

---

### 📌 So Why Does Mosh Say We Don't Use Templates Much Now?

In **modern full-stack development**, Django often acts as a **backend API**, and we use something like:

- **React**, **Vue**, or **Next.js** as the frontend
- Django only returns **JSON**, not rendered HTML

So you’ll focus more on **Django REST Framework** later in the course to build APIs.

But if you ever build:

- A blog
- A company website
- A dashboard for admin
  Templates are still **super useful** — especially for internal tools or quick MVPs.

---
