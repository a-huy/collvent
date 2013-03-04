$('#status-select').change(function() {
    var csrftoken = getCookie('csrftoken')
    var new_status = $(this).val();
    console.log('/api/events/invite/' + jsonVars['invite_uuid'] + '/');
    $.ajaxSetup({
        crossDomain: false,
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
                xhr.setRequestHeader('X-HTTP-Method-Override', 'PUT');
            }
        }
    });
    $.ajax({
        type: 'POST',
        async: false,
        url: '/api/events/invite/' + jsonVars['invite_uuid'] + '/',
        data: [
            { name: 'status', value: new_status }
        ],
        success: function(output) {
            document.location.reload();
        },
        error: function(err) {
        }
    });

});

// function loadGoogleMapsApi() {
//     var gmScript = document.createElement('script');
//     gmScript.type = 'text/javascript';
//     gmScript.src = 'https://maps.googleapis.com/maps/api/js?key=' + 
//         jsonVars['google_api_key'] + '&sensor=true&callback=initializeMap';
//     document.body.appendChild(gmScript);
// }

// function initializeMap() {
//     var evt_loc = new google.maps.LatLng(jsonVars['loc_lat'], jsonVars['loc_lng']);
//     var mapOptions = {
//         zoom: 15,
//         center: evt_loc,
//         mapTypeId: google.maps.MapTypeId.ROADMAP
//     };
//     event_map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
//     var markerOptions = {
//         map: event_map,
//         position: evt_loc
//     };
//     loc_marker = new google.maps.Marker(markerOptions);
// }

// window.onload = loadGoogleMapsApi;