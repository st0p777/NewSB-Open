$(function () {
    $('#id_deadline').datepicker({
        multipleDates: 2,
        multipleDatesSeparator: ' - ',
        minDate: new Date(),
        language: 'ru',
        dateFormat: 'yyyy-mm-dd',
        firstDay: 0,
        toggleSelected: false,
        range: true,
        timepicker: true,
        minutesStep: 5,
        clearButton: true,
        onSelect(formattedDate, date, inst) {
            inst.hide();
        },
        altField: $('#alt'),
        altFieldDateFormat: 'yyyy-mm-dd'
    });

});