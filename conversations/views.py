# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponseBadRequest, \
    HttpResponse
from django.template import RequestContext
import django.contrib.auth as auth
import conversations.models as cm

def ben_test(request):
	allConversationsOBJ = cm.Conversation.objects.all()

	template_vars = {
		'allConvoOBJ' : allConversationsOBJ,
	}

	return render_to_response('testConversations.html', template_vars, context_instance=RequestContext(request))