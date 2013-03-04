$('#start-date, #end-date').each(function() {
    $(this).datepicker();
});

$('#add-invite').click(function() {
    var input_html = '<p><input type="text" /></p>';
    $('#invite-list').append(input_html)
});