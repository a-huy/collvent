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
        user = invites_lib.get_or_create_user(ident_type, identifier)
