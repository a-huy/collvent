# Create your views here.

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponseBadRequest, \
    HttpResponse
from django.template import RequestContext
import django.contrib.auth as auth
import events.models as em
import django.utils.timezone as dut
from datetime import timedelta
import groups

def create_event(request):
    template_vars = {}
    return render_to_response('create_event.html', template_vars,
        context_instance=RequestContext(request))

def list_events(request):
    template_vars = {}
    events = em.Event.objects.all().order_by('start_date')
    weekGroups = groups.groupIntoWeeks(events)

    template_vars['weekGroups'] = weekGroups
    
    return render_to_response('list.html', template_vars,
        context_instance=RequestContext(request))

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
