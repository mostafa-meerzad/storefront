**Django: A High-Level Python Web Framework**

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
