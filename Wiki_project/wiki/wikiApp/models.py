from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE


# Create your models here.


class WikiModel(models.Model):
    entryName = models.CharField(max_length=50)
    entryInfo = models.CharField(max_length=10000)
    foreignKey = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return f"{self.entryName} {self.entryInfo}"
