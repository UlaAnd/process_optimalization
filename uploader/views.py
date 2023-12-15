from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django_q.tasks import async_task

from uploader.forms import UploadForm
from uploader.models import Image
from uploader.tasks import send_email_task


def upload_form_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            start_process(form.cleaned_data, instance.id)
            return redirect("success")
    else:
        form = UploadForm()
    return render(request, "uploader/uploader.html", {"form": form})


def start_process(valid_data: dict, image_id: str) -> None:
    Image.objects.get(id=image_id)
    email = valid_data["mail"]
    message = "Your file is uploaded!"
    async_task(send_email_task, email, message)


def success(request: HttpRequest) -> HttpResponse:
    return render(request, "uploader/success.html")
