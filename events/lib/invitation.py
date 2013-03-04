from django.core.mail import send_mail
import accounts.models as accounts_models

def get_or_create_user(type, identifier):
    try:
        kwargs = { type: identifier }
        user = accounts_models.User.objects.get(**kwargs)
    except accounts_models.User.DoesNotExist:
        temp_user = accounts_models.User.objects.create_user(**kwargs)