from django.core.mail import send_mail
from django.conf import settings
import accounts.models as accounts_models

def get_or_create_user(ident_type, identifier):
    try:
        kwargs = { ident_type: identifier }
        user = accounts_models.User.objects.get(**kwargs)
        return user
    except accounts_models.User.DoesNotExist:
        temp_user = accounts_models.User.objects.create_user(**kwargs)
        return temp_user

def send_invitation(ident_type, invite):
    if ident_type == 'email':
        event = invite.event
        host_name = event.host.get_full_name()
        title = event.title
        url = 'http://%s/invitation/%s/' % (settings.DOMAIN, invite.uuid)
        subject = '%s invited you to the event "%s"' % (host_name, title)
        message = 'You can access the event page here: %s' % url
        send_mail(subject, message, 'noreply@%s' % settings.DOMAIN, [invite.user.email])
    else:
        pass
