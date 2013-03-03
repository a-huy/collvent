from django.db import models
import conversations.constant as constant


# Create your models here.
class EventConversation:
        event = models.ForeignKey('Event')
        title = models.CharField(max_length = constant.MAX_SIZE_NAME)

class ConversationContent:
        title = models.CharField(max_length = constant.MAX_SIZE_CONTENT)
        url = models.CharField(max_length = constant.MAX_SIZE_URL)
        owner = models.ForeignKey('User')
        converstaion = models.ForeignKey('Conversation')

class ConversationMessage
        conversation = models.ForeignKey('Conversation')
        owner = models.ForeignKey('Person')
        message = models.CharField(max_length = MAX_SIZE_MESSAGE)
        postDate = models.DateTime()

