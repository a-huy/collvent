from django.db import models
from django.conf import settings
import base.models as base_models
import conversations.constants as constants
import events.models as events_models

class Conversation(base_models.Base):
        event = models.ForeignKey(events_models.Event)
        title = models.CharField(max_length=constants.MAX_SIZE_NAME)

class ConversationContent(base_models.Base):
        title = models.CharField(max_length=constants.MAX_SIZE_CONTENT)
        url = models.CharField(max_length=constants.MAX_SIZE_URL)
        owner = models.ForeignKey(settings.AUTH_USER_MODEL)
        conversation = models.ForeignKey(Conversation)

class ConversationMessage(base_models.Base):
        conversation = models.ForeignKey(Conversation)
        owner = models.ForeignKey(settings.AUTH_USER_MODEL)
        message = models.CharField(max_length=constants.MAX_SIZE_MESSAGE)
        postDate = models.DateTimeField()
