from django.shortcuts import render_to_response
from django.http import HttpResponseBadRequest, HttpResponse
from django.template import RequestContext
from django import forms
import events.models as events_models

def create_event(request):
    template_vars = {}
    return render_to_response('create_event.html', template_vars,
        context_instance=RequestContext(request))

def list_events(request):
    template_vars = {}
    return render_to_response('list.html', template_vars,
        context_instance=RequestContext(request))