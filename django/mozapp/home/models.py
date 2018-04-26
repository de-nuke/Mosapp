from django.db import models

# Create your models here.


class MainImage(models.Model):
    photo = models.ImageField(blank=False, null=False)

    # def __str__(self):
