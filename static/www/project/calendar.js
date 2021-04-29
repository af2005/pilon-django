import { Calendar } from '@fullcalendar/core';

document.addEventListener('DOMContentLoaded', function () {

    function formatDate(d) {
        let date = [
            d.getFullYear(),
            ('0' + (d.getMonth() + 1)).slice(-2),
            ('0' + d.getDate()).slice(-2)
        ].join('-');
        date += " " + ('0' + d.getHours()).slice(-2) + ":" + ('0' + d.getMinutes()).slice(-2);
        return date

    }

    function get_form_value(dom_name) {
        return $("#calendar-event-modal input[name=" + dom_name + "]").val();
    }

    function set_form_value(dom_name, value) {
        return $("#calendar-event-modal input[name=" + dom_name + "]").val(value);
    }

    function open_edit_event_modal(eventInfo) {
        $("#calendar-event-modal-heading").text("Edit event " + eventInfo.event.title);
        $("#calendar-event-modal button[name='delete-button']").removeClass("d-none");
        $("#calendar-event-modal button[name='delete-button']").unbind().click(function () {
            send_delete_event(eventInfo);
            calendar.refetchEvents();
            $("#calendar-event-modal").modal('hide');
        });
        set_form_value("title", eventInfo.event.title);
        set_form_value("description", eventInfo.event.extendedProps.description);
        set_form_value("old_start", formatDate(eventInfo.event.start));
        set_form_value("old_end", formatDate(eventInfo.event.end));
        set_form_value("start", formatDate(eventInfo.event.start));
        set_form_value("end", formatDate(eventInfo.event.end));
        set_form_value("event_id", eventInfo.event.extendedProps.event_id);
        $("#calendar-event-modal button[name='submit']").html("Edit Event");

        $("#calendar-event-modal-form").unbind().on("submit", function (event) {
            event.preventDefault();
            const e = {};
            e.event = {};
            e.oldEvent = {};
            e.event.extendedProps = {};
            e.event.title = get_form_value("title");
            e.event.startStr = get_form_value("start");
            e.event.endStr = get_form_value("end");
            e.oldEvent.startStr = get_form_value("old_start");
            e.oldEvent.endStr = get_form_value("old_end");
            e.event.extendedProps.description = get_form_value("description");
            e.event.extendedProps.event_id = get_form_value("event_id");
            e.event.extendedProps.existed = get_form_value("existed");
            e.event.extendedProps.calendar = get_form_value("calendar_slug");
            send_edited_event(e);
            calendar.refetchEvents();
        });

        flatpickr("#calendar-event-modal input[name='start']", {
            enableTime: true,
            dateFormat: "Y-m-d H:i",
            time_24hr: true,
        });

        flatpickr("#calendar-event-modal input[name='end']", {
            enableTime: true,
            dateFormat: "Y-m-d H:i",
            time_24hr: true,
        });
        //$("#calendar-event-modal input[name='start']")._flatpickr.jumpToDate(eventInfo.event.start);
        $("#calendar-event-modal").modal('show');

    }

    function open_create_event_modal() {
        $("#calendar-event-modal-heading").text("Create new event");
        $("#calendar-event-modal button[name='delete-button']").addClass("d-none");
        $("#calendar-event-modal input[name='title']").val("");
        $("#calendar-event-modal input[name='description']").val("");
        $("#calendar-event-modal input[name='old_start']").val();
        $("#calendar-event-modal input[name='old_end']").val();
        $("#calendar-event-modal input[name='start']").val("");
        $("#calendar-event-modal input[name='end']").val("");
        $("#calendar-event-modal button[name='submit']").html("Create Event");
        $("#calendar-event-modal-form").unbind().on("submit", function (event) {
            event.preventDefault();
            const e = {};
            e.title = get_form_value("title");
            e.start = get_form_value("start");
            e.end = get_form_value("end");
            e.description = get_form_value("description");
            send_new_event(e);
            calendar.refetchEvents();
        });

        flatpickr("#calendar-event-modal input[name='start']", {
            enableTime: true,
            dateFormat: "Y-m-d H:i",
            time_24hr: true,
        });

        flatpickr("#calendar-event-modal input[name='end']", {
            enableTime: true,
            dateFormat: "Y-m-d H:i",
            time_24hr: true,
        });
        //$("#calendar-event-modal input[name='start']")._flatpickr.jumpToDate(eventInfo.event.start);
        $("#calendar-event-modal").modal('show');

    }

    function send_new_event(eventInfo) {
        $.ajax({
            type: 'POST',
            url: "{% url 'schedule_create_event' %}",
            dataType: 'json',
            data: {
                "title": eventInfo.title,
                "start": eventInfo.start,
                "end": eventInfo.end,
                "calendar_slug": "{{ project.key }}",
                "description": eventInfo.description
            },
            success: function (result) {
                calendar.refetchEvents();
                $("#calendar-event-modal").modal('hide');
            },
            error: function (req, status, error) {
                console.log(error);
            }
        });
        return false;
    }

    function send_edited_event(eventInfo) {
        $.ajax({
            type: 'POST',
            url: "{% url 'schedule_edit_event' %}",
            dataType: 'json',
            data: {
                "title": eventInfo.event.title,
                "description": eventInfo.event.extendedProps.description,
                "event_start": eventInfo.event.startStr,
                "event_end": eventInfo.event.endStr,
                "old_event_start": eventInfo.oldEvent.startStr,
                "old_event_end": eventInfo.oldEvent.endStr,
                "event_id": eventInfo.event.extendedProps.event_id,
                "existed": eventInfo.event.extendedProps.existed,
                "calendar": eventInfo.event.extendedProps.calendar,

            },
            success: function (result) {
                calendar.refetchEvents();
                $("#calendar-event-modal").modal('hide');
            },
            error: function (req, status, error) {
                console.log(error);
            }
        });
        return false;
    }

    function send_delete_event(eventInfo) {
        $.ajax({
            type: 'POST',
            url: "{% url 'schedule_delete_event' %}",
            dataType: 'json',
            data: {
                "event_id": eventInfo.event.extendedProps.event_id,
                "calendar": eventInfo.event.extendedProps.calendar,
            },
            success: function (result) {
                calendar.refetchEvents();
                $("#calendar-event-modal").modal('hide');
            },
            error: function (req, status, error) {
                console.log(error);
            }
        });
        return false;
    }


    const calendarEl = document.getElementById('full-calendar');
    let calendar = new Calendar(calendarEl, {
        events: '/schedule/occurrences/?calendar_slug={{ project.key }}',
        timeZone: 'local',
        editable: true,
        initialView: 'dayGridMonth',
        firstDay: 1,
        themeSystem: 'bootstrap',
        eventTimeFormat: { // like '14:30:00'
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
        },
        headerToolbar: {
            start: 'prev,next today',
            center: 'title',
            end: 'dayGridMonth,dayGridWeek,timeGridDay createButton'
        },
        bootstrapFontAwesome: {
            prev: ' bi bi-chevron-left',
            next: ' bi bi-chevron-right',
            prevYear: ' bi bi-chevron-double-left',
            nextYear: ' bi bi-chevron-double-right',
            close: 'bi bi-x'
        },
        buttonText: {
            today: 'now',
            month: 'M',
            week: 'W',
            day: 'D',
            list: 'list'
        },
        buttonIcons: {
            month: 'left-single-arrow',
            next: 'right-single-arrow',
            prevYear: 'left-double-arrow',
            nextYear: 'right-double-arrow'
        },
        customButtons: {
            createButton: {
                text: 'Add...',
                click: open_create_event_modal,
            }
        },
        navLinks: true,
        navLinkDayClick: function (date) {
            calendar.changeView('timeGridDay');
            calendar.gotoDate(date);

        },
        eventResize: send_edited_event,
        eventDrop: send_edited_event,
        eventClick: open_edit_event_modal,
    });
    calendar.render();
});
