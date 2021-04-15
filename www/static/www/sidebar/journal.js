const journalDatePicker = function () {
    const now = new Date();
    const first_of_month = new Date(now.getFullYear(), now.getMonth(), 1);
    const last_of_month = new Date(now.getFullYear(), now.getMonth() + 1, 0);

    function getJournalPagesInDateRange(selectedDates){
        const parameter = {
            "date_created__gte": selectedDates[0].toISOString(),
            "date_created__lte": selectedDates[1].toISOString()
        }
        return $.getJSON(Urls.journalpageList()+"?"+$.param(parameter), writeListToDOM)
    }

    function writeListToDOM(data){
        let sItems = "";
        $.each( data, function( key, val ) {
            sItems += `<li> ${val.name}</li>`
        });
        $("#sidebar-journal-pages").html(sItems);
    }
    flatpickr("#sidebar-journal-calendar", {
        enableTime: false,
        dateFormat: "Y-m-d",
        inline: true,
        onValueUpdate: function(selectedDates, dateStr, instance) {
            if (selectedDates.length === 2){
                getJournalPagesInDateRange(selectedDates)
            }
        },
        mode: "range",
        "locale": {
            "firstDayOfWeek": 1 // start week on Monday
        },
        defaultDate: [first_of_month, last_of_month]
    });
}();
