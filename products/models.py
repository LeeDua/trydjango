from django.db import models


class Product(models.Model):
    prop1 = models.TextField()
    title = models.CharField(max_length=120,default='hey')
