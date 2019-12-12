from django.db import models


class ImgUpload(models.Model):
    img = models.ImageField(upload_to="img/")
    name = models.TextField()

    class Meta:
        pass
