from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.managers import CollventUserManager
import accounts.constants as constants
from django.utils import timezone
import events.models as eventModels

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
            proper_first = self.first_name[0].upper() + self.first_name[1:]
            proper_last = self.last_name[0].upper() + self.last_name[1:]
            return ' '.join([proper_first, proper_last])
        else:
            if self.email:
                return self.email
            elif self.phone:
                return self.phone

    def get_short_name(self):
        return self.first_name or self.uuid

    def __unicode__(self):
        id_str = self.phone or self.email or self.uuid
        return id_str

    def has_perm(self, perm, obj=None):
        if self.is_admin: return True
        return False

    @property
    def password_set(self):
        return not self.check_password(' ')

    def getEvents(self):
        events = []
        events.extend(self.event_set.filter(start_date__gte=timezone.now()))
        for invitation in self.invitation_set.filter(event__start_date__gte=timezone.now()):
            events.append(invitation.event)
        events.sort(key=lambda event: event.start_date)
        return events

    def getEventRsvp(self, event):
        invitation = eventModels.Invitation.objects.filter(user=self, event=event)
        if invitation:
            status = invitation[0].status
        else:
            status = eventModels.Invitation._meta.get_field_by_name('status')[0].default
        return eventModels.Invitation.STATUS[status][1]

    def get_account_name(self):
        if not self.password_set:
            if self.email:
                guestName = self.email
            elif self.phone:
                guestName = self.phone
            name = 'Guest (%s)' % guestName
        else:
            name = self.get_full_name()
        return name