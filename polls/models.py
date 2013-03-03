from django.db import models
from django.conf import settings
import base.models as b_base
import polls.constants as constants
import events.models as events_models

class Poll(b_base.Base):
        title = models.CharField(max_length=constants.MAX_SIZE_TITLE)
        event = models.ForeignKey(events_models.Event)

class Choice(b_base.Base):
        poll = models.ForeignKey(Poll)
        text = models.CharField(max_length=constants.MAX_SIZE_CHOICE)
        votes = models.IntegerField()

class Vote(b_base.Base):
        user = models.ForeignKey(settings.AUTH_USER_MODEL)
        choice = models.ForeignKey(Choice)
        liked = models.BooleanField()
