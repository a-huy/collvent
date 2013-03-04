import json
from urllib import urlencode
import urllib2

# Takes a place object and returns its long / lat as a dict
# If the update flag is passed, the Place object is updated 
# with the coordinates
def geocode_place(place):
    endpoint = 'https://maps.googleapis.com/maps/api/geocode/json?'
    addr = '%s+%s+%s+%s' % (
        place.street_addr.replace(' ', '+'),
        place.city,
        place.state,
        place.zip_code
    )
    options = {
        'address': addr,
        'sensor': 'true'
    }
    response = urllib2.urlopen('%s%s' % (endpoint, urlencode(options))).read()
    data = json.loads(response)
    if data['status'] != 'OK': return None
    coords = data['results'][0]['geometry']['location']
    return coords