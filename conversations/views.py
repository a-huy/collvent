# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponseBadRequest, \
    HttpResponse
from django.template import RequestContext
import django.contrib.auth as auth
import conversations.models as cm
from django.contrib.auth.decorators import login_required

@login_required
def ben_test(request):

	messages = cm.ConversationMessage.objects.all().order_by('created_date')
	template_vars = {
		'allmessages' : messages
	}
	return render_to_response('testConversations.html', template_vars, 
		context_instance=RequestContext(request))


