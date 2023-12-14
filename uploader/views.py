from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django_q.tasks import async_task

from uploader.forms import UploadForm
from uploader.tasks import send_email_task


def contact(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UploadForm(request.POST)
        if form.is_valid():
            send_email(form.cleaned_data)
            return redirect("success")
    else:
        form = UploadForm()
    return render(request, "uploader/uploader.html", {"form": form})


def send_email(valid_data: dict) -> None:
    email = valid_data["email"]
    message = (
        f"You have received a contact form.\n"
        f"Email: {valid_data['email']}\n"
        f"{valid_data['message']}\n"
    )
    async_task(send_email_task, email, message)


def success(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Success!")
