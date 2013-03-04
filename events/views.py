# Create your views here.

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponseBadRequest, \
    HttpResponse
from django.template import RequestContext
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required
import events.models as events_models
import groups

def create_event(request):
    template_vars = {}
    return render_to_response('create_event.html', template_vars,
        context_instance=RequestContext(request))

@login_required
def list_events(request):
    template_vars = {}
    events = request.user.getEvents()
    for event in events:
        status = request.user.getEventRsvp(event)
        event.rsvp_status = status

    weekGroups = groups.groupIntoWeeks(events)

    template_vars['weekGroups'] = weekGroups
    
    return render_to_response('list.html', template_vars,
        context_instance=RequestContext(request))

def invitation(request, invite_uuid):
    try:
        invite = events_models.Invitation.objects.get(uuid=invite_uuid)
    except events_models.Invitation.DoesNotExist:
        return HttpResponseBadRequest('Invitation was not found.')
    user = auth.authenticate(hash=invite.user.uuid)
    if user:
        auth.login(request, user)
        return redirect('/events/%s' % invite.event.uuid)
    else: return HttpResponseBadRequest('Could not validate invitation.')

def event(request, event_uuid):
    try:
        event = events_models.Event.objects.get(uuid=event_uuid)
    except events_models.Event.DoesNotExist:
        return HttpResponseBadRequest('Event does not exist')
    template_vars = {
        'event': event,
    }
    return render_to_response('event.html', template_vars,
        context_instance=RequestContext(request))
