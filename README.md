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
3. **Give Execute Permissions to Formats File**
    ```bash
    chmod +x ./formats
    ```
4. **Run Formats File Code**
    ```bash
    ./formats lint
    ```

## Save Dependencies

Record the list of all the Python packages required by your application into a requirements file using:
```bash
pip freeze > requirements.txt
```

## Run Django-Q Monitoring

1. **Start Django-Q Cluster**
    ```bash
    python manage.py qcluster
    ```
2. **Start Django-Q Monitor**
    ```bash
    python manage.py qmonitor
    ```
Please follow the above commands