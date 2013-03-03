from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.managers import CollventUserManager
import accounts.constants as constants

class User(AbstractBaseUser):
    uuid = models.CharField(
        max_length=constants.USER_HASH_MAX_LENGTH,
        unique=True,
        db_index=True,
    )
    email = models.EmailField(
        max_length=constants.USER_EMAIL_MAX_LENGTH,
        unique=True,
        db_index=True,
        blank=True,
        null=True
    )
    phone = models.CharField(
        max_length=constants.USER_PHONE_MAX_LENGTH,
        unique=True,
        db_index=True,
        blank=True,
        null=True
    )
    first_name = models.CharField(max_length=constants.USER_NAME_MAX_LENGTH)
    last_name = models.CharField(max_length=constants.USER_NAME_MAX_LENGTH)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    avatar = models.CharField(max_length=constants.USER_AVATAR_MAX_LENGTH)

    objects = CollventUserManager()

    USERNAME_FIELD = 'uuid'

    def get_full_name(self):
        if self.first_name and self.last_name:
            return ' '.join([self.first_name, self.last_name])
        else:
            return self.uuid

    def get_short_name(self):
        return self.first_name or self.uuid

    def __unicode__(self):
        id_str = self.phone or self.email or self.uuid
        return id_str

    def has_perm(self, perm, obj=None):
        if self.is_admin: return True
        return False
