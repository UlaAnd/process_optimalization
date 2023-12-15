from django import forms

from uploader.models import Image


class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["mail", "file"]
