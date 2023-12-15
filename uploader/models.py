from django.db import models


class Image(models.Model):
    mail = models.CharField(max_length=50)
    file = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
