from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .managers import UserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=225, blank=True, null=True)
    first_name = models.CharField(max_length=225, blank=True, null=True)
    last_name = models.CharField(max_length=225, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.email

