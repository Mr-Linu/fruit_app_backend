from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
        email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password=None):

        user = self.create_user(
        email,
        password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class AppUser(AbstractBaseUser):
    email = models.EmailField(
    verbose_name='email address',
    max_length=255,
    unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    otp = models.CharField(max_length=6 , null=True, blank=True)

    objects = AppUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255,  null=True)
    phone = models.CharField(max_length=255)
    Contact = models.PositiveIntegerField()
    image = models.ImageField(default="", null=True, blank=True)


    def __str__(self):
        return self.full_name