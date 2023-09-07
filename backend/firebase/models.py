from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import uuid

from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name  = "User"
        # verbose_name_plural  = "Users"

    uuid = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="UUID")
    username = models.CharField(_("username"), unique=True, max_length=64)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.uuid
    

