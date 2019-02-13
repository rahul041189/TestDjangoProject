# Create your models here.
from django.db import models

class AppDetails(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name + ' : ' + self.description

class Screen(models.Model):
    appdetails = models.ForeignKey(AppDetails, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    is_fav = models.BooleanField(default=False)
    def __str__(self):
        return self.title

