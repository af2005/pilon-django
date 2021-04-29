const sidebarDatePicker = function () {
    const start_of_week = getMonday(new Date());
    const end_of_week = new Date(start_of_week).setDate(start_of_week.getDate()+6)

    function getJournalPagesInDateRange(selectedDates) {
        if (selectedDates.length === 2) {
            //increase end date by one day to include this day

            selectedDates[1].setDate(selectedDates[1].getDate() + 1);
            const parameter = {
                "date__gte": selectedDates[0].toISOString(),
                "date__lte": selectedDates[1].toISOString()
            }
            $.getJSON("/rest/journal-page?" + $.param(parameter), writeListToDOM)
        }
    }

    function getMonday(d) {
        d = new Date(d);
        const day = d.getDay(),
            diff = d.getDate() - day + (day === 0 ? -6 : 1); // adjust when day is sunday
        return new Date(d.setDate(diff));
    }


    function writeListToDOM(data) {
        let sItems = "";
        //$(".sidebar-lower-content .flatpickr-day").removeClass("page-available")
        $.each(data, function (key, val) {
            let created_date = new Date(val["date_created"]);
            let timeblob = `<time dateTime="2021-4-23" class="sidebar-time-icon"><div class="day">${created_date.getDate()}</div></time>`;
            sItems += `<li><a class="sidebar-journal-item" href="${val["absolute_url"]}">${timeblob}<span class="ps-2">${val["name"]}</span></a></li>`
            //$(".sidebar-lower-content .flatpickr-day").eq(created_date.getDay()).addClass("page-available")
        });
        $("#sidebar-journal-pages").html(sItems);
    }

    const flatpickrInstance = flatpickr("#sidebar-journal-calendar", {
        enableTime: false,
        dateFormat: "Y-m-d",
        inline: true,
        onReady: getJournalPagesInDateRange,
        onValueUpdate: getJournalPagesInDateRange,
        mode: "range",
        "locale": {
            "firstDayOfWeek": 1 // start week on Monday
        },
        defaultDate: [start_of_week, end_of_week],
        monthSelectorType: "static",
        shorthandCurrentMonth: true,
    });
    return {flatpickrInstance:flatpickrInstance}
}();
