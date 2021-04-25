const homepage = function () {

    const events = function () {
        function get(calendar_slug) {
            const now = new Date();
            const dateInAWeek = new Date()
            dateInAWeek.setDate(now.getDate() + 7);
            const parameter = {
                "calendar_slug": calendar_slug,
                "start": now.toISOString(),
                "end": dateInAWeek.toISOString()
            }
            $.getJSON("/schedule/api/occurrences?" + $.param(parameter), write)
        }

        function template(entity) {
            const startDate = new Date(entity["start"]);
            const months = ["Jan", "Feb", "Mar", "Apr", "May"]
            return `<div>
                <time class="icon align-self-center">
                    <div class="month">${startDate.getMonth()}</div>
                    <div class="day">${startDate.getDate()}</div>
                    <div class="weekday">Sun</div>
                </time>
                ${entity["title"]}
            </div>
            `
        }

        function write(data) {
            let events = "";
            $.each(data, function (key, entity) {
                console.log(entity)
                events += template(entity);
            });
            $("#homepage-events").append(events);
        }

        return {
            get: get
        }
    }();

    const activity = function () {
        function template(entity) {
            const action = entity["date-created"] === entity["date-modified"] ? "created" : "modified";
            //TODO I need the last updater as a person, not only creator.
            return `<div class="d-flex text-muted list-group-item">
            <i class="display-6 bi ${iconClass(entity["entity_type"])}"></i>
            <p class="small lh-sm">
                <strong class="text-gray-dark">@username</strong>
                ${action} 
                ${entity["name"]}
            </p>
         </div>`
        }

        function get(parentId) {
            const minDateModified = new Date()
            minDateModified.setDate(minDateModified.getDate() - 7)
            const parameter = {
                //TODO This needs to be different. Now only direct children of a project will be loaded
                "parent": parentId,
                "date_modified__gte": minDateModified.toISOString()
            }
            $.getJSON("/rest/entity?" + $.param(parameter), write)
        }

        function iconClass(entityType) {
            switch (entityType) {
                case "WikiPage":
                    return "bi-file-text";
                case "JournalPage":
                    return "bi-journal";
                case "Comment":
                    return "bi-chat"
            }
        }

        function write(data) {
            let activities = "";
            $.each(data, function (key, entity) {
                activities += template(entity);
            });
            $("#homepage-activity").append(activities);
        }

        return {
            get: get
        }
    }();

    return {
        getActivity: activity.get,
        getEvents: events.get
    }
}();

