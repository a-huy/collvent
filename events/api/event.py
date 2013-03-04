import datetime
from django.http import HttpResponse, HttpResponseBadRequest
import base.api.base as base
import events.models as events_models

class EventCreateApi(base.RestView):
    def POST(self, request, *args, **kwargs):
        if 'title' not in request.POST or not request.POST['title']:
            return HttpResponseBadRequest('Each place must have a title.')

        start_date = datetime.datetime.strptime(request.POST['start_date'], '%m/%d/%Y %H:%M')
        end_date = datetime.datetime.strptime(request.POST['end_date'], '%m/%d/%Y %H:%M')

        data = {
            'title': request.POST['title'],
            'location_id': request.POST['place_id'],
            'start_date': start_date,
            'end_date': end_date,
            'host': request.user
        }
        if 'description' in request.POST and request.POST['description']:
            data['description'] = request.POST['description']

        new_event = events_models.Event(**data)
        try:
            curr_event = events_models.Event.objects.get(host=new_event.host,
                title=new_event.title)
            return HttpResponseBadRequest('Event already exists.')
        except events_models.Event.DoesNotExist:
            new_event.save()
            return base.ApiResponse({ 'event_uuid': new_event.uuid })
