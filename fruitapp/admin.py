from django.contrib import admin

from fruitapp.models import Prediction, Results

# Register your models here.
admin.site.register(Prediction)
admin.site.register(Results)