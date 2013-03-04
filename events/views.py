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


def ben_test(request):
	alleventsOBJ = em.Event.objects.all().order_by('start_date')
	eventTree = {}

	thisWeek = []
	nextWeek = []
	rest = []

	endThisWeek = dut.now() - timedelta(hours=8)
	endNextWeek = dut.now()

	while True:
		if endThisWeek.strftime("%A") == 'Wednesday':
			endNextWeek = endThisWeek + timedelta(days=7)
			break
		endThisWeek += timedelta(days=1)


	for x in alleventsOBJ:
		if x.start_date < endThisWeek:
			thisWeek.append(x)			
		elif x.start_date < endNextWeek:
			nextWeek.append(x)
		else:
			rest.append(x)

	eventTree['thisWeek'] = thisWeek
	eventTree['nextWeek'] = nextWeek
	eventTree['rest'] = rest

	template_vars = {
		'eventTree' : eventTree,
		'endNext' : endNextWeek,
		'endThis' : endThisWeek

	}
	return render_to_response('testEvent.html', template_vars, context_instance=RequestContext(request))
