# What is Django?

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It follows the **Model-View-Template (MVT)** architectural pattern and comes with a wide range of built-in features, reducing the need for third-party libraries.

## Why Use Django?

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
pipenv install django
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

if you are already inside a directory and want to start your Django app init, don't specify the `project_name` instead provide `./`

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

A Django project consists of multiple apps.
each app provides certain functionality just like your smartphone with apps each one providing a specific functionality.

you can find all the installed apps in the `yourProjectName/settings.py` path e.x: `storefront/settings.py`

```python

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', gives us an admin interface for managing our data
    'django.contrib.auth', used for authenticating users
    'django.contrib.contenttypes', will come soon in the course
    'django.contrib.sessions', kinda legacy and not used in newer versions of django projects
    'django.contrib.messages', for displaying one time notifications to the users
    'django.contrib.staticfiles', for serving static assets like iamges, icons
]

```

To create an app, run:

```bash
python manage.py startapp app_name
```

for our `storefront` project just run `python manage.py startapp playground` in the terminal

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

then we need to register our newly created app to the `projectName/settings.py` in `INSTALLED_APPS` list

```python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'playground'
]
```

### What is an App in Django?

In Django, an **app** is a self-contained module that handles a specific function or feature of a larger web application. Apps are designed to be reusable and modular, allowing developers to build complex web applications by combining multiple apps.

A Django **project** is the entire web application, which can contain multiple **apps**. Each app has its own models, views, templates, static files, and other logic, making it an independent component that can be plugged into different projects.

---

## **1. Understanding the Django App Structure**

When you create an app using the `startapp` command, Django generates a directory with a predefined structure:

```plaintext
my_project/
│
├── my_app/  # This is the app
│   ├── migrations/  # Database migration files
│   │   ├── __init__.py
│   ├── __init__.py  # Marks this directory as a Python package
│   ├── admin.py  # Configuration for the Django Admin panel
│   ├── apps.py  # App configuration
│   ├── models.py  # Database models
│   ├── tests.py  # Unit tests
│   ├── views.py  # Application logic (controllers)
│   ├── urls.py  # URL routing for the app
│   ├── templates/  # HTML templates (optional)
│   ├── static/  # Static files (CSS, JS, images)
```

Each of these files serves a specific purpose in the app's functionality.

---

## **2. How to Create an App in Django?**

To create an app inside a Django project, follow these steps:

### **Step 1: Navigate to the Django Project**

First, make sure you are inside your Django project directory. If you don’t have a project yet, create one:

```sh
django-admin startproject my_project
cd my_project
```

### **Step 2: Create a New App**

Run the following command:

```sh
python manage.py startapp my_app
```

This will create a directory named `my_app` with the structure mentioned earlier.

### **Step 3: Register the App in `settings.py`**

Open `my_project/settings.py` and add the app to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_app',  # Registering the new app
]
```

---

## **3. Components of a Django App**

A Django app consists of multiple components:

### **(a) Views (`views.py`)**

Views handle requests and return responses, typically rendering HTML templates or JSON responses.

Example:

```python
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def say_hello(request):
    return HttpResponse("Hello World")
```

---

### **(b) URL Configuration (`urls.py`)**

let's say in our `storefront` project whenever the url `localhost:8000/playground/hello` is requested the view function should be called and "Hello World" should be displayed to the user.

Each app can have its own `urls.py`, which maps URLs to views.

now create a `url.py` file in your app `playground` directory

Example:

```python
from django.urls import path #import path function
from . import views #import views module so we can reference our view function

# now set a special variable that Django listens for "name is important" all in lowercase
# it is a list of pattern objects
# use th path function to create a url-pattern object
# what we have here is basically called a url-configuration object
urlpatterns = [

    path('url/path', views.your_view_handler),
    path('playground/hello', views.say_hello) # for our app
]
```

Now, include this app’s URLs in the project’s main `urls.py`:

in the "urls.py" module the instruction for adding another url-pattern is already provided

```python
from django.contrib import admin
from django.urls import include, path
# import "include" function so we can use our url pattern from our app
#
# "playground/" means any url that starts with "playground" will be handled by this "playground" app
# Django chops off the first part of the url "playground/hello" and sends the "hello" to the url-configuration-module in "playground" app
# this way there is no need to have the full url path in the url-configuration-module

# every route must end wit "/"!
urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include("playground.urls")),
    path('pathName/', include('your_app.urls')),  # Including app's URLs
]
```

---

### **(c) Templates (`templates/`)**

Django uses the template system to render HTML files dynamically.

Example:
Create a file `my_app/templates/home.html`:

for our project `playground/templates/hello.html`

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Home</title>
  </head>
  <body>
    <h1>Welcome to Django!</h1>
  </body>
</html>
```

or

```html
<!-- in the template you can have logic or render data dynamically -->
{% if name %}
<!-- name is dynamic and provided in the views module render method  -->
<h1>Hello {{ name }}</h1>

{% else %}
<h1>Hello World</h1>

{% endif %}
```

Modify the view to use the template:

```python
def home(request):
    return render(request, 'home.html')
```

or

```python
def say_hello(request):
    # return HttpResponse("Hello World")
    # return render(request, "hello.html") # render template with no dynamic data provided
    return render(request, "hello.html", {"name": "Mostafa"}) # name is provided as dynamic data

```

---

### **(d) Models (`models.py`)**

Django models define the structure of your database tables. They are Python classes that map to database tables using Django’s ORM (Object-Relational Mapping).

Example:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

To apply this model to the database, run:

```sh
python manage.py makemigrations
python manage.py migrate
```

### **(e) Static Files (`static/`)**

Django apps can include CSS, JavaScript, and images inside a `static/` directory.

Example:
Store a CSS file at `my_app/static/style.css` and use it in templates:

```html
<link rel="stylesheet" type="text/css" href="{% static 'style.css' %}" />
```

Make sure to configure `STATIC_URL` in `settings.py`:

```python
STATIC_URL = '/static/'
```

---

## **4. Why Use Multiple Apps?**

A Django project can be broken down into multiple apps, each handling a different responsibility.  
For example, in an **e-commerce project**, you might have:

- `users` app → Handles authentication and user profiles.
- `products` app → Manages product listings and categories.
- `orders` app → Handles customer orders and payments.

This modular approach makes development, maintenance, and code reusability easier.

---

## **5. Reusing Django Apps**

One of Django's strengths is that apps can be reused in different projects. To do this:

- Keep the app self-contained.
- Use Django’s app configuration (`apps.py`) to make it portable.
- Avoid hardcoding project-specific settings.

For example, a **blog app** can be used in multiple projects simply by installing it and including its URLs.

---

## **6. Best Practices for Django Apps**

- Keep each app focused on a **single responsibility**.
- Organize templates inside the app (e.g., `my_app/templates/my_app/home.html`).
- Use Django’s **app configuration** in `apps.py` for better structure.
- Avoid **circular dependencies** by carefully structuring imports.
- Write **tests** for your app in `tests.py` to ensure functionality.

---

## **7. Common Mistakes When Working with Django Apps**

1. **Not Registering the App in `INSTALLED_APPS`**

   - If you forget to add the app to `settings.py`, migrations won’t work.

2. **Misplacing Templates and Static Files**

   - Make sure templates are inside `templates/my_app/` to avoid conflicts.

3. **Forgetting to Include URLs in the Project’s `urls.py`**

   - Apps need to be linked in the main `urls.py` for their views to be accessible.

4. **Circular Imports in Models or Views**
   - If two models import each other, use `from app_name import models` instead.

---

## **Conclusion**

A Django app is a modular component that encapsulates specific functionality within a project. By using multiple apps, developers can build scalable, maintainable, and reusable web applications. Each app consists of models, views, templates, static files, and other configurations, making it an independent and self-contained unit.

Would you like me to explain anything in more detail or provide a practical example? 🚀

## Debugging Django Apps in VScode

Open VScode click the Debug icon, then create a `launch.json` file from the suggested menu select `Python Debugger` then from the second menu select `Django App` and finally select the path to `manage.py` from your main project directory.

To make sure our debugger doesn't conflict with our app server on port:8000.

in the `args` array add a port number like `9000` as a string

```json
 "args": ["runserver", "9000"],
```

in your code set break-points and then run debugger `F5` in VScode, when your break-points arrive code execution stops and from there on you can execute your code line by line.

As a best practice remove your break-points after you're done with debugging

in VScode you can run your project for example Our Django project without running the `python manage.py runserver` by just using Run Without Debug from the Run menu or `Ctr + F5`.

## Debug Django Apps using Django-Debug-Toolbar

[Django-Debug-Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

just follow the instructions
