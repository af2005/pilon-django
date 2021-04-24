const homepage = function () {

    function getActivity(parentId) {
        const minDateModified = new Date()
        minDateModified.setDate(minDateModified.getDate() - 7)
        const parameter = {
            //TODO This needs to be project. Otherwise only direct children of a project will be loaded
            "parent": parentId,
            "date_modified__gte": minDateModified.toISOString()
        }
        $.getJSON("/rest/entity?" + $.param(parameter), writeActivityToDOM)
    }

    function iconClass(entityType){
        switch (entityType){
            case "WikiPage": return "bi-file-text";
            case "JournalPage": return "bi-journal";
            case "Comment": return "bi-chat"
        }
    }

    function activityTemplate(entity) {
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

    function writeActivityToDOM(data) {
        let activities = "";

        $.each(data, function (key, entity) {
            activities += activityTemplate(entity);
        });
        $("#homepage-activity").append(activities);
    }

    return {getActivity: getActivity}
}();

