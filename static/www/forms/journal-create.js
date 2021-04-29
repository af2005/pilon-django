const markdownForm = document.getElementById("markdown-create-form");
markdownForm.addEventListener("submit", function (e) {
    e.preventDefault();
    markdownForm.markdown.value = editor.getMarkdown();
    console.log(markdownForm.markdown.value);
    markdownForm.submit();
})

const dateSelector = function () {
    function updateDateField(date) {
        $('#page-date').val(date[0].toISOString());
    }

    const flatpickrObject = flatpickr("#page-date-picker", {
        enableTime: false,
        inline: false,
        onValueUpdate: updateDateField,
        dateFormat: "Y-m-d",
        locale: {
            "firstDayOfWeek": 1 // start week on Monday
        },
    });

    return {
        flatpickrObject: flatpickrObject
    }
}();
