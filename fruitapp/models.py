from django.db import models

from user.models import AppUser


class Prediction(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    fruit_name = models.CharField(max_length=255)
    accuracy = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    prediction = models.CharField(max_length=255)
    image = models.ImageField(default="")
    date_created = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.fruit_name} prediction by {self.user} '


class Results(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    fruit = models.CharField(max_length=255)
    accuracy = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    Description = models.CharField(max_length=255)
    image = models.ImageField(default="")
    date_created = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.fruit} results by {self.user} '


class Image(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField()
    image_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.image_name} image uploaded by {self.user} '