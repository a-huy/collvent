from uuid import uuid4
from django.contrib.auth.models import BaseUserManager
from django.core.validators import validate_email

class CollventUserManager(BaseUserManager):
    def create_user(self, uuid=None, email=None, phone=None, password=None):
        if not email and not phone:
            raise ValueError('Users must have either email or phone')

        validate_email(email)
        if not uuid: uuid = uuid4().hex

        user = self.model(email=CollventUserManager.normalize_email(email),
            phone=phone,
            uuid=uuid
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password, uuid=None, email=None, phone=None):
        user = self.create_user(uuid=uuid, email=email, phone=phone, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
