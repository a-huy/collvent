$('#login-submit').click(function() {
    var csrftoken = getCookie('csrftoken');
    var identifier = $('#identifier').val();
    var password = $('#password').val();
    var next = $('#next').val();

    if (!identifier || identifier == '') {
        $('#login-form').notify({
            message: 'Please enter your email or phone number.',
            type: 'error',
            timeOut: 5000
        });
        return;
    }

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
        url: '/login/',
        data: [
            { name: 'identifier', value: identifier },
            { name: 'password', value: password },
            { name: 'next', value: next }
        ],
        success: function(output) {
            if (!next || next == '') {
                document.location = '/events/list/'
            }
            else { document.location = next }
        },
        error: function(err) {
            $('#login-form').notify({
                message: err.responseText,
                type: 'error',
                timeOut: 5000
            });
        }
    });
});