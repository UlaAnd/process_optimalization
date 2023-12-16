# Project Title: File Uploader with Async Function

This project facilitates file uploading with an asynchronous function. Once the file upload process is completed, the system automatically sends an email notification. 

The deployed version of the application can be accessed at: https://process-optimalization.onrender.com
## Prerequisites

Ensure that Python 3.11 is installed on your machine to avoid any compatibility issues.

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
4. **Commands for Local Running**

   First terminal:
   ```bash
    python manage.py runserver 
   ```
   Second terminal:
   ```bash
    python manage.py qcluster
   ```

1. **Give Execute Permissions to Scripts**
    ```bash
    chmod +x ./formats
    ```
2. **Run Scripts**
    ```bash
    ./formats lint
    ```

## Save Dependencies

If you want to record the list of all Python packages required by your application, you can do so into a requirements file using:
```bash
pip freeze > requirements.txt
``