from django.contrib.auth.models import BaseUserManager

from ..enums.role_enums import UserRole
from ..exceptions.data_exceptions import DBFieldError


class CustomUserManager(BaseUserManager):
    ...