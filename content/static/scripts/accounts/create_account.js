$('#create-submit').click(function() {
    var csrftoken = getCookie('csrftoken');
    var first = $('#input-first').val();
    var last = $('#input-last').val();
    var email = $('#input-email').val();
    var phone = $('#input-phone').val();
    var pass = $('#input-pass').val();
    var conf = $('#pass-conf').val();

    if (!first || first == '') {
        $('#create-form').notify({
            message: 'You must provide your first name.',
            type: 'error',
            timeOut: 5000
        });
        return;
    }
    if (!last || last == '') {
        $('#create-form').notify({
            message: 'You must provide your last name.',
            type: 'error',
            timeOut: 5000
        });
        return;
    }
    if ((!email || email == '') && (!phone || phone == '')) {
        $('#create-form').notify({
            message: 'You must submit either an email or a phone number.',
            type: 'error',
            timeOut: 5000
        });
        return;
    }
    if (!pass || pass == '') {
        $('#create-form').notify({
            message: 'Password cannot be empty.',
            type: 'error',
            timeOut: 5000
        });
        return;
    }
    if (pass.length < 6) {
        $('#create-form').notify({
            message: 'Password must be at least 6 characters.',
            type: 'error',
            timeOut: 5000
        });
        return;
    }
    if (pass != conf) {
        $('#create-form').notify({
            message: 'Your passwords do not match.',
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
        url: '/api/accounts/user/',
        data: [
            { name: 'first_name', value: first },
            { name: 'last_name', value: last },
            { name: 'email', value: email },
            { name: 'phone', value: phone },
            { name: 'password', value: pass }
        ],
        success: function(output) {
            $('#create-form').notify({
                message: 'Account has been successfully created!',
                type: 'error',
                timeOut: 5000,
                refresh: true
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