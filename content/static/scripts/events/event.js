function loadGoogleMapsApi() {
    var gmScript = document.createElement('script');
    gmScript.type = 'text/javascript';
    gmScript.src = 'https://maps.googleapis.com/maps/api/js?key=' + 
        jsonVars['google_api_key'] + '&sensor=true&callback=initializeMap';
    document.body.appendChild(gmScript);
}

function initializeMap() {
    var evt_loc = new google.maps.LatLng(jsonVars['loc_lat'], jsonVars['loc_lng']);
    var mapOptions = {
        zoom: 15,
        center: evt_loc,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    event_map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
    var markerOptions = {
        map: event_map,
        position: evt_loc
    };
    loc_marker = new google.maps.Marker(markerOptions);
}

window.onload = loadGoogleMapsApi;