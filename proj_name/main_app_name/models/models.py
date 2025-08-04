import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import CustomUserManager

class User(AbstractBaseUser):
    # PROVIDED FIELD : password, is_active, last_login
    email = models.EmailField(null=True, unique=True)
    nickname = models.TextField()
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'

    # objects = CustomUserManager()  # ManagerClass()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']