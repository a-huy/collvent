$('#pass-submit').click(function() {
    var csrftoken = getCookie('csrftoken');
    var curr_pass = $('#curr-pass').val();
    var new_pass = $('#new-pass').val();
    var conf_pass = $('#conf-pass').val();

    if (!curr_pass) {
        $(document).notify({
            message: 'Enter your current password to change it.',
            type: 'error',
            timeOut: 5000
        });
        return;
    }
    if (!new_pass) {
        $(document).notify({
            message: 'New password cannot be blank.',
            type: 'error',
            timeOut: 5000
        });
        return;
    }
    if (new_pass != conf_pass) {
        $(document).notify({
            message: 'Passwords do not match.',
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
                xhr.setRequestHeader('X-HTTP-Method-Override', 'PUT');
            }
        }
    });
    $.ajax({
        type: 'POST',
        async: false,
        url: '/api/accounts/user/' + jsonVars['uuid'] + '/',
        data: [
            { name: 'password', value: new_pass }
        ],
        success: function(output) {
            $(document).notify({
                message: 'Password has been changed!',
                type: 'error',
                timeOut: 5000,
            });
        },
        error: function(err) {
            $(document).notify({
                message: err.responseText,
                type: 'error',
                timeOut: 5000
            });
        }
    });
});