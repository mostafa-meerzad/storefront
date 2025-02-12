**Django: A High-Level Python Web Framework**

### What is Django?
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It follows the **Model-View-Template (MVT)** architectural pattern and comes with a wide range of built-in features, reducing the need for third-party libraries.

### Why Use Django?
1. **Batteries-Included** – Django provides built-in features like authentication, ORM (Object-Relational Mapping), an admin panel, form handling, and more.
2. **Security** – It helps developers avoid common security pitfalls like SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF).
3. **Scalability** – Django is used by major websites like Instagram and Disqus, proving its ability to handle high traffic.
4. **Rapid Development** – It promotes reusable components, making development faster and more efficient.
5. **Well-Documented** – Django has extensive and well-structured documentation, making it easy to learn and troubleshoot.

---

## Getting Started with Django

### Installing Django
To install Django, ensure you have Python installed. Then, use pip to install Django:
```bash
pip install django
```

You can verify the installation by running:
```bash
django-admin --version
```

### Creating a Django Project
To start a new Django project, use the following command:
```bash
django-admin startproject project_name
```
This will create a directory structure like this:
```
project_name/
    manage.py
    project_name/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
- **manage.py** – A command-line utility for managing the project.
- **settings.py** – Stores configuration settings.
- **urls.py** – Handles URL routing.
- **wsgi.py/asgi.py** – Entry points for WSGI/ASGI servers.

### Running the Development Server
Navigate into your project directory and run:
```bash
python manage.py runserver
```
By default, this starts a local server at `http://127.0.0.1:8000/`.

---

## Django Basics

### Creating an App
A Django project consists of multiple apps. To create an app, run:
```bash
python manage.py startapp app_name
```
This generates the following structure:
```
app_name/
    migrations/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```
- **models.py** – Defines database models.
- **views.py** – Handles request/response logic.
- **admin.py** – Configures the admin interface.

### Defining Models
A model represents a table in the database. Example:
```python
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
```
After defining models, run:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Registering Models in Admin
To manage models via the Django admin panel, register them in `admin.py`:
```python
from django.contrib import admin
from .models import Movie

admin.site.register(Movie)
```
Then, create a superuser to access the admin panel:
```bash
python manage.py createsuperuser
```

### Views and URL Routing
A simple view function:
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```
Add the route in `urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
]
```
Now, visiting `http://127.0.0.1:8000/` will display "Hello, Django!"

---
This covers the foundational concepts of Django. Next, we can dive into templates, forms, authentication, and more!

