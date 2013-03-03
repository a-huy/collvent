// Notify
(function($) {
    $.fn.notify = function(options){
        var settings = {
            type: 'alert',   // type should equal 'error', 'alert', 'loading', or 'success'
            message: '',
            timeOut: null,   // time to display, in ms
            effect: 'blind', // effect for jQuery show() method
            refresh: false
        }

        $.extend(settings, options);

        return this.each(function(){
            var $notify = $(this).find('.notify').first();

            clearTimeout($notify.data('notifyTimeoutId'));
            $notify.stop(true, true);
            $notify.removeClass('error loading alert success');
            $notify.html(settings.message).addClass(settings.type);

            //for some reason, using :hidden or :visible doesn't work here.
            //we have to directly look at the css display property
            if ($notify.is(':hidden')) {
                $notify.show(settings.effect);
            }

            if (settings.timeOut) {
                $notify.data('notifyTimeoutId', setTimeout(function() { 
                    $notify.hide(settings.effect); 
                    if (settings.refresh) document.location.reload();
                }, settings.timeOut));
            }
        });
    }
})(jQuery);

// getCookie (taken from django docs https://docs.djangoproject.com/en/dev/ref/contrib/csrf/)
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Taken from the CSRF Django docs (https://docs.djangoproject.com/en/dev/ref/contrib/csrf/)
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
