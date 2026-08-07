# Feasto - Developer Notes

## Day 1 - Project Setup

### Goal

## Set up the Django development environment and create the first application.

## 1. Create a Virtual Environment

### Command

```bash
python -m venv .venv
```

### Why?

A virtual environment creates an isolated Python environment for this project.

### Benefits

- Keeps project dependencies separate.
- Prevents version conflicts between projects.
- Makes the project portable.

---

## 2. Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### How do I know it's active?

The terminal shows:

```text
(.venv)
```

---

## 3. Install Django

### Command

```bash
pip install django
```

### Why?

Django is the web framework used to build the Feasto application.

### Verify Installation

```bash
django-admin --version
```

---

## 4. Create a Django Project

### Command

```bash
django-admin startproject Feasto
```

### Why?

Creates the main Django project containing the overall configuration.

### Files Created

- settings.py → Project settings
- urls.py → Main URL routing
- asgi.py → ASGI configuration
- wsgi.py → WSGI configuration

---

## 5. Create a Django App

### Command

```bash
python manage.py startapp feastoApp
```

### Why?

Apps divide a project into smaller, manageable modules.
For now:

- Project = Feasto
- App = feastoApp

### Files Created

- models.py
- views.py
- admin.py
- apps.py
- tests.py
- migrations/

---

## What I Learned Today

- A virtual environment keeps dependencies isolated.
- Django is a Python web framework.
- A Django project contains the overall configuration.
- A Django app contains a specific feature or module.
- `manage.py` is used to execute Django management commands.
- `python manage.py runserver` is used to run the project

---

## Commands Learned

```bash
python -m venv .venv
.venv\Scripts\activate
pip install django
django-admin startproject Feasto
python manage.py startapp feastoApp
python manage.py runserver
```

---

## Next Step

- Register `feastoApp` inside `INSTALLED_APPS` in `settings.py`.

# Configure Django Settings

## File Modified

`Feasto/settings.py`

## Changes Made

### 1. Registered the Application

Added `feastoApp` to the `INSTALLED_APPS` list.

### Why Was This Needed?

Django only recognizes the built-in applications by default. By registering `feastoApp`, Django becomes aware of the app and includes it in the project.

After registration, Django can:

- Detect models for database migrations.
- Load templates and static files from the app.
- Register the app with the Django Admin.
- Execute app-specific configurations.

Without adding the app to `INSTALLED_APPS`, Django ignores the app completely.

---

### 2. Configured Static Files

Configured the `STATIC_URL` setting.

### Why Was This Needed?

Static files include resources that do not change dynamically, such as:

- CSS
- JavaScript
- Images
- Fonts

`STATIC_URL` defines the base URL used to access these static files in the browser.

Example:

- CSS
- JavaScript
- Images

During development, Django serves these files using this URL.

---

## What I Learned

- `settings.py` is the central configuration file of a Django project.
- Every custom app must be registered in `INSTALLED_APPS`.
- If an app is not registered, Django will not recognize its models, templates, or other resources.
- `STATIC_URL` is used to serve static assets like CSS, JavaScript, and images.

## One-Line Summary

Registered `feastoApp` with the Django project and configured the URL for serving static files.

# Project URL Configuration

## File Modified

`Feasto/urls.py`

## Changes Made

- Imported the functionality required to connect URL patterns from another app.
- Connected the main Django project to the `feastoApp`.
- Kept the Django Admin route available.

## Why Was This Needed?

By default, the Django project only knows about the Admin page. To allow the application to handle user requests, the project must be connected to the app. This enables the app to manage its own URLs while the project acts as the main entry point.

## What I Learned

- The Django project receives all incoming requests first.
- The project forwards requests to the appropriate app.
- Each app manages its own URL routing.
- This structure keeps the project modular, organized, and easy to maintain.

## Real-World Analogy

Think of the Django project as the **reception desk** of a company.

- The visitor enters the company.
- The receptionist receives the visitor.
- The receptionist sends the visitor to the correct department.
- The department handles the visitor's request.
  Similarly, the Django project receives every request and forwards it to the correct app.

## One-Line Summary

Connected the main Django project with `feastoApp` so that the app can handle website requests.
# User Navigation & Registration Flow

## Files Modified
- `feastoApp/views.py`
- `feastoApp/urls.py`
- `templates/signup.html`
- `templates/signin.html`

---

## Changes Made

### 1. Created View Functions

Created view functions to:
- Display the Home page.
- Open the Sign Up page.
- Open the Sign In page.
- Process the Sign Up form.

### Why Was This Needed?

A view function contains the application's logic. It receives a request from the browser, processes it, and returns an appropriate response such as an HTML page or data. :contentReference[oaicite:0]{index=0}

---

### 2. Configured URL Routing

Created URL patterns for:
- Home page
- Sign Up page
- Sign In page
- Sign Up form submission

### Why Was This Needed?

URL routing connects browser requests to the appropriate view function, allowing users to navigate between different pages. :contentReference[oaicite:1]{index=1}

---

### 3. Designed the Sign Up Page

Created a registration form to collect:
- Username
- Password
- Email
- Mobile Number
- Address

Used the **POST** method to securely submit user information and included CSRF protection. :contentReference[oaicite:2]{index=2}

### Why Was This Needed?

The Sign Up page collects user details that will later be stored in the database.

---

### 4. Designed the Sign In Page

Created a login form containing:
- Username
- Password

Configured the form to submit user credentials. :contentReference[oaicite:3]{index=3}

### Why Was This Needed?

Allows registered users to enter their login credentials for authentication.

---

### 5. Processed Form Data

Retrieved the submitted form values from the Sign Up page and displayed them in the response to verify that data was being received correctly. :contentReference[oaicite:4]{index=4}

### Why Was This Needed?

This verifies that the form submission works correctly before integrating the database.

---

## What I Learned

- Views contain the application's business logic.
- URL patterns map browser requests to view functions.
- HTML forms collect user input.
- The POST method is used to submit sensitive user data.
- CSRF protection secures form submissions.
- Form data can be accessed through the request object.

---

## One-Line Summary

Implemented the basic user navigation and registration flow by creating views, configuring URL routing, designing Sign Up and Sign In pages, and processing submitted form data.