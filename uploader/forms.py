from django import forms


class UploadForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={"rows": 5}))
    # file = forms.FileField()
