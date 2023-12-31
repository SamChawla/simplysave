# Getting Started with Simply Save Django Project

## Setup Virtual Environment

1. Create a virtual environment using Python:

    ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment:

    - For Windows:

        ```bash
        venv\Scripts\activate
        ```

    - For Linux/Mac:

        ```bash
        source venv/bin/activate
        ```

## Install Django

3. Install Django using pip:

    ```bash
    pip install django
    ```

## Create Django Project

4. Create a new Django project named "simply_save" (the dot avoids creating an extra folder):

    ```bash
    django-admin startproject simply_save .
    ```

## Test the Project

5. Test if the project is running:

    ```bash
    python manage.py runserver
    ```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser to see if the project is up and running.

## Create Bookmark App

6. Create Bookmark App

    ```bash
    python manage.py startapp bookmark
    ```

7. Register Bookmark inside INSTALLED_APP in settings.
    
    "bookmark.apps.BookmarkConfig"

8. Add URLS

