# Project Title: File Uploader with Async Function

This project is a file uploader with an asynchronous function. Once the file upload process is completed, the system automatically sends an email notification.

The deployed version of the application can be accessed on the following URL: https://process-optimalization.onrender.com

## Prerequisites

Ensure you have Python 3.11 installed on your machine to avoid any compatibility issues.

## Installation

1. **Install Required Modules**
    ```bash
    pip install -r requirements.txt
    ```
2. **Perform Database Migration**
    ```bash
    python manage.py migrate
    ```
3. **Create Django Superuser**
   ```bash
   python manage.py createsuperuser
   ```
4. **Mailgun Configuration**
    If you want Mailgun to work for sending emails, please fill this with your data in settings.py file. 
    ```python
    ANYMAIL = {
        "MAILGUN_API_KEY": "",
        "MAILGUN_SENDER_DOMAIN": "",
    }

    SERVER_EMAIL = "example@example.com"
    DEFAULT_FROM_EMAIL = "example@example.com"
    ```

5. **Commands for Local Running**
  First terminal:
   ```bash
    python manage.py runserver 
   ```
   Second terminal:
   ```bash
    python manage.py qcluster
   ```

6. **Give Execute Permissions to linter scripts**
    ```bash
    chmod +x ./formats
    ```
7. **Run Scripts**
    ```bash
    ./formats lint
    ```

## Save Dependencies

If you want to record the list of all Python packages required by your application, you can do so into a requirements file using:
```bash
pip freeze > requirements.txt
```