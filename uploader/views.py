from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from uploader.forms import UploadForm
from uploader.tasks import start_process


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


def success(request: HttpRequest) -> HttpResponse:
    return render(request, "uploader/success.html")
