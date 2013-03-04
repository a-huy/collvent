$('#start-date, #end-date').each(function() {
    $(this).datepicker();
});

$('#start-time, #end-time').each(function() {
    $(this).timepicker({ 'timeFormat': 'H:i' });
});

$('#add-invite').click(function() {
    var input_html = '<p><input type="text" /></p>';
    $('#invite-list').append(input_html)
});

$('#event-submit').click(function() {
    var csrftoken = getCookie('csrftoken');
    var title = $('#event-title').val();
    var start_date = $('#start-date').val();
    var start_time = $('#start-time').val();
    var end_date = $('#end-date').val();
    var end_time = $('#end-time').val();
    var description = $('#event-desc').val();
    var thumbnail = $('#event-thumb').val();
    var name = $('#addr-name').val();
    var street_addr = $('#event-street-addr').val();
    var city = $('#event-city').val();
    var state = $('#event-state').val();
    var zip = $('#event-zip').val();

    var invites = $('#invite-list input');

    if (!title || title == '') {
        $('#create-form').notify({
            message: 'Enter a title for the event.',
            type: 'error',
            timeOut: 5000
        });
        return;
    }
    if (!start_date || !end_date) {
        $('#create-form').notify({
            message: 'Events must have a start and end date.',
            type: 'error',
            timeOut: 5000
        });
        return;
    }
    start_datetime = clean_datetime(start_date, start_time);
    end_datetime = clean_datetime(end_date, end_time);

    if (!name || name == '') {
        $('#create-form').notify({
            message: 'Enter a name of your location.',
            type: 'error',
            timeOut: 5000
        });
        return;
    }

    addr_data = [
        { name: 'name', value: name }
    ]
    if (street_addr) { addr_data.push({ name: 'street_addr', value: street_addr }); }
    if (city) { addr_data.push({ name: 'city', value: city }); }
    if (state) { addr_data.push({ name: 'state', value: state }); }
    if (zip) { addr_data.push({ name: 'zip', value: zip }); }

    event_data = [
        { name: 'title', value: title },
        { name: 'start_date', value: start_datetime },
        { name: 'end_date', value: end_datetime }
    ]
    if (description) { event_data.push({ name: 'description', value: description }); }
    if (thumbnail) { event_data.push({ name: 'thumbnail', value: thumbnail }); }

    $.ajaxSetup({
        crossDomain: false,
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    $.ajax({
        type: 'POST',
        async: false,
        url: '/api/events/place/',
        data: addr_data,
        success: function(msg) {
            event_data.push({ name: 'place_id', value: msg['place_id']});
            $.ajax({
                type: 'POST',
                async: false,
                url: '/api/events/event/',
                data: event_data,
                success: function(msg) {
                    invites.each(function() {
                        var ident = $(this).val();
                        console.log(ident)
                        if (ident && ident != '') {
                            $.ajax({
                                type: 'POST',
                                async: true,
                                url: '/api/events/invite/',
                                data: [
                                    { name: 'event_uuid', value: msg['event_uuid'] },
                                    { name: 'identifier', value: ident }
                                ],
                                success: function() { console.log(ident); }
                            });
                        }
                    });
                    document.location = '/events/' + msg['event_uuid'] + '/';
                },
                error: function(err) {
                    $('#create-form').notify({
                        message: err.responseText,
                        type: 'error',
                        timeOut: 5000
                    });
                }
            });
        },
        error: function(err) {
            $('#create-form').notify({
                message: err.responseText,
                type: 'error',
                timeOut: 5000
            });
        }
    });

});

function clean_datetime(date, time) {
    if (!time || time == '') { time = '00:00'; }
    return date + ' ' + time;
}