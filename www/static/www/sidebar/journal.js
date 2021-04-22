const journalDatePicker = function () {
    const now = new Date();
    const first_of_month = new Date(now.getFullYear(), now.getMonth(), 1);
    const last_of_month = new Date(now.getFullYear(), now.getMonth() + 1, 0);

    function getJournalPagesInDateRange(selectedDates) {
        if (selectedDates.length === 2) {
            //increase end date by one day to include this day

            selectedDates[1].setDate(selectedDates[1].getDate() + 1);
            const parameter = {
                "date_created__gte": selectedDates[0].toISOString(),
                "date_created__lte": selectedDates[1].toISOString()
            }
            $.getJSON("/rest/journal-page?" + $.param(parameter), writeListToDOM)
        }
    }

    function writeListToDOM(data) {
        let sItems = "";
        $.each(data, function (key, val) {
            let created_date = new Date(val["date_created"]);
            sItems += `<a class="sidebar-journal-item" href="${val["absolute_url"]}"> <i class="bi bi-journal text-dark"></i><span class="sidebar-journal-item-date">${created_date.getDate()}</span>${val["name"]}</a>`
        });
        $("#sidebar-journal-pages").html(sItems);
    }

    flatpickr("#sidebar-journal-calendar", {
        enableTime: false,
        dateFormat: "Y-m-d",
        inline: true,
        onReady: getJournalPagesInDateRange,
        onValueUpdate: getJournalPagesInDateRange,
        mode: "range",
        "locale": {
            "firstDayOfWeek": 1 // start week on Monday
        },
        defaultDate: [first_of_month, last_of_month],
        monthSelectorType: "static",
        shorthandCurrentMonth: true,
    });
    return {

    }
}();
