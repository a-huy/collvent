from django.db import models
import base.models as b_base
import events.constant as constant

# Create your models here.
class Event(b_base.Base): 
	host = models.ForeignKey('User')
        start_date = models.DateField
        end_date = models.DateField
        description = models.TextField(max_length = constant.MAX_DESCRIPTION)
        location = models.ForeignKey('Address')

class Place(b_base.Base):
        name = models.CharField(max_length = constant.MAX_NAME)
        street_addr = models.CharField(null=True)
        city = models.CharField(null=True)
        state = models.CharField(null=True)
        zip = models.IntegerField(null=True)
        longitude = models.DecimalField(null=True)
        latitude = models.DecimalField(null=True)

class Invitation(b_base.Base):
        event = models.ForeignKey('Event')
        user = models.ForeignKey('User')

