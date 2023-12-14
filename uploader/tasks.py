from time import sleep

from django.core.mail import BadHeaderError, send_mail

from process_optimalization.settings import DEFAULT_FROM_EMAIL


def send_email_task(to: str, message: str) -> None:
    try:
        sleep(5)
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
