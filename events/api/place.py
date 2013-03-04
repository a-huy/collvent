from django.http import HttpResponse, HttpResponseBadRequest
import base.api.base as base
import events.models as events_models
import events.lib.place as place_lib

class PlaceCreateApi(base.RestView):
    def POST(self, request, *args, **kwargs):
        if 'name' not in request.POST or not request.POST['name']:
            return HttpResponseBadRequest('Each place must have a name.')

        data = {
            'name': request.POST['name']
        }
        new_place = events_models.Place(**data)
        if 'street_addr' in request.POST and request.POST['street_addr']:
            new_place.street_addr = request.POST['street_addr']
            new_place.city = request.POST['city']
            new_place.state = request.POST['state']
            new_place.zip_code = request.POST['zip']

            coords = place_lib.geocode_place(new_place)
            new_place.latitude = coords['lat']
            new_place.longitude = coords['lng']

        try:
            curr_place = events_models.Place.objects.get(latitude=new_place.latitude,
                longitude=new_place.longitude)
            ret_id = curr_place.pk
        except events_models.Place.DoesNotExist:
            new_place.save()
            ret_id = new_place.pk
        return base.ApiResponse({
            'place_id': ret_id,
        })