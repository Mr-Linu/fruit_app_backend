from django.db import models

from user.models import AppUser


class Prediction(models.Model):
    user = models.ForeignKey(AppUser)
    fruit_name = models.CharField(max_length=255)
    accuracy = models.DecimalField()
    prediction = models.CharField(max_length=255)
    image = models.ImageField(default="")
    date_created = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)


class Results(models.Model):
    user = models.ForeignKey(AppUser)
    fruit = models.CharField(max_length=255)
    accuracy = models.DecimalField()
    Description = models.CharField(max_length=255)
    image = models.ImageField(default="")
    date_created = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)


class Image(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField()
    date_created = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(AppUser)