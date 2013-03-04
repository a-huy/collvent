# Create your views here.

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponseBadRequest, \
    HttpResponse
from django.template import RequestContext
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required
from django.conf import settings
import events.models as events_models
import conversations.models as conversations_models
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

    convo = conversations_models.Conversation.objects.filter(event = event)
    content = []
    messages = []

    print "conversations list: ", convo
    for x in convo:
        content.extend(conversations_models.ConversationContent.objects.filter(conversation = x).order_by("created_date"))
        messages.extend(conversations_models.ConversationMessage.objects.filter(conversation = x).order_by("created_date"))

    messages.sort(key=lambda messages: messages.created_date)

    messageGroup = []
    groupedSet = []
    for x in messages:
        if groupedSet:
            if groupedSet[0].conversation.title == x.conversation.title:
                groupedSet.append(x)
            else:
                messageGroup.append(groupedSet)
                groupedSet = []
                groupedSet.append(x)
        else:
            messageGroup.append(groupedSet)
            groupedSet = []
            groupedSet.append(x)
        if x == messages[-1]:
            messageGroup.append(groupedSet)


    try:
        if request.user != event.host:
            invite = events_models.Invitation.objects.get(event=event, user=request.user)
        else:
            invite = None
    except events_models.Invitation.DoesNotExist:
        return HttpResponseBadRequest('Current user is not invited to this event.')
        
    template_vars = {
        'event': event,
        'content': content,
        'messages': messages,
        'messageGroup': messageGroup,

        'json_vars': {
            'google_api_key': settings.GOOGLE_API_KEY,
            'loc_lng': str(event.location.longitude),
            'loc_lat': str(event.location.latitude),
        },
    }
    if invite:
        template_vars['invite'] = invite
        template_vars['json_vars']['invite_uuid'] = str(invite.uuid)
    return render_to_response('event.html', template_vars,
        context_instance=RequestContext(request))
