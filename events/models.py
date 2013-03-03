from django.db import models
import base.models as b_base
import events.constants as constants
from django.conf import settings

class Place(b_base.Base):
        name = models.CharField(max_length=constants.MAX_NAME)
        street_addr = models.CharField(max_length=constants.STREET_MAX_LENGTH, null=True)
        city = models.CharField(max_length=constants.CITY_MAX_LENGTH, null=True)
        state = models.CharField(max_length=constants.STATE_MAX_LENGTH, null=True)
        zip_code = models.IntegerField(null=True)
        longitude = models.CharField(max_length=constants.LOC_MAX_LENGTH, null=True)
        latitude = models.CharField(max_length=constants.LOC_MAX_LENGTH, null=True)

class Event(b_base.Base): 
        host = models.ForeignKey(settings.AUTH_USER_MODEL)
        start_date = models.DateField(null=True)
        end_date = models.DateField(null=True)
        description = models.TextField(max_length=constants.MAX_DESCRIPTION)
        location = models.ForeignKey(Place)

class Invitation(b_base.Base):
        event = models.ForeignKey(Event)
        user = models.ForeignKey(settings.AUTH_USER_MODEL)

