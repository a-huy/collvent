from uuid import uuid4
from django.core.validators import validate_email
from django.http import HttpResponse, HttpResponseBadRequest
import base.api.base as base
import events.models as events_models
import accounts.lib.user as user_lib
import events.lib.invitation as invite_lib

class InvitationCreateApi(base.RestView):
    def POST(self, request, *args, **kwargs):
        if 'event_uuid' not in request.POST or not request.POST['event_uuid']:
            return HttpResponseBadRequest('Specify an event for the invitation.')
        if 'identifier' not in request.POST or not request.POST['identifier']:
            return HttpResponseBadRequest('Missing identifier.')
        identifier = request.POST['identifier']
        ident_type = ''
        try:
            validate_email(identifier)
            ident_type = 'email'
        except ValidationError:
            try:
                identifier = user_lib.clean_us_phone_number(identifier)
                ident_type = 'phone'
            except ValidationError:
                return HttpResponseBadRequest('Identifier is neither an email nor a phone number')
        user = invite_lib.get_or_create_user(ident_type, identifier)
        try:
            event = events_models.Event.objects.get(uuid=request.POST['event_uuid'])
            if user.uuid == event.host.uuid:
                return HttpResponseBadRequest('The host is already a part of the event.')
            invite = events_models.Invitation.objects.get(user=user, event=event)
            return HttpResponseBadRequest('User has already been invited to the event.')
        except events_models.Event.DoesNotExist:
            return HttpResponseBadRequest('Event could not be found.')
        except events_models.Invitation.DoesNotExist:
            pass
        data = {
            'uuid': uuid4().hex,
            'user': user,
            'event': event
        }
        new_invite = events_models.Invitation(**data)
        new_invite.save()
        invite_lib.send_invitation(ident_type, new_invite)
        return HttpResponse()

class InvitationApi(base.RestView):
    def PUT(self, request, invite_uuid, *args, **kwargs):
        try:
            invite = events_models.Invitation.objects.get(uuid=invite_uuid)
        except events_models.Invitation.DoesNotExist:
            return HttpResponseBadRequest('Invitation could not be found.')
        if 'status' in request.POST and request.POST['status']:
            invite.status = request.POST['status']
        invite.save()
        return HttpResponse()
