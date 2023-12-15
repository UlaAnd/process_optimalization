from time import sleep

from django.core.mail import BadHeaderError, send_mail
from django_q.tasks import async_task

from process_optimalization.settings import DEFAULT_FROM_EMAIL
from uploader.models import Image


def start_process(valid_data: dict, image_id: str) -> None:
    Image.objects.get(id=image_id)
    email = valid_data["mail"]
    message = "Your file is uploaded!"
    async_task(send_email_task, email, message)


def send_email_task(to: str, message: str) -> None:
    try:
        sleep(30)
        print("About to send_mail")
        send_mail(
            "Subject of the email",  # Replace with your subject
            message,
            DEFAULT_FROM_EMAIL,
            [to],
            fail_silently=False,  # Set to True if you want errors to be ignored
        )
    except BadHeaderError:
        print("BadHeaderError")
    except Exception as e:
        print(e)
