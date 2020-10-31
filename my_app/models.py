from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have a email id')

        user = self.model(
            email = self.normalize_userid(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given phone and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.save(using=self._db)
        return user


class Doctor(AbstractBaseUser):

    is_staff = models.BooleanField(default=False)
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    email = models.EmailField(max_length=150,verbose_name = 'email address',unique=True)
    password = models.CharField(max_length=150)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return self.fname