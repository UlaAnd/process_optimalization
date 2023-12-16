from time import sleep

from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django_q.tasks import async_task

from uploader.models import Image


def start_process(valid_data: dict, image_id: int) -> None:
    Image.objects.get(id=image_id)
    email = valid_data["mail"]
    async_task(send_email_task, email, image_id)


def send_email_task(to: str, image_id: int) -> None:
    try:
        sleep(30)
        image = Image.objects.get(id=image_id)
        message = f"Your file is uploaded! Id of your file is: {image.id}"
        print("About to send_mail")
        send_mail(
            "Your file",
            message,
            settings.DEFAULT_FROM_EMAIL,
            [to],
            fail_silently=False,
        )
    except BadHeaderError:
        print("BadHeaderError")
    except Exception as e:
        print(e)
