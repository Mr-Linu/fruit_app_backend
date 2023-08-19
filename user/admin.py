from django.contrib import admin

from user.models import AppUser, Profile

# Register your models here.
admin.site.register(AppUser)
admin.site.register(Profile)