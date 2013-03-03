from django.db import models
import base.models as b_base
import polls.constant as constant

# Create your models here.
class Poll(b_base.Base):
        title = models.CharField(max_length = constant.MAX_SIZE_TITLE)
        event = models.ForeignKey('Event')

class Choice(b_base.Base):
        poll = models.ForeignKey('Poll')
        text = models.CharField(max_length = constant.MAX_SIZE_CHOICE)
        votes = models.IntegerField()

class Vote(b_base.Base):
        user = models.ForeignKey('User')
        choice = models.ForeignKey('Choice')
        liked = models.BooleanField()
