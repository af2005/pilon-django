const markdownForm = function () {
    $("#markdown-form").submit(function (e) {
        e.preventDefault();
        editor.changeMode("wysiwyg");
        this.markdown.value = editor.getMarkdown();
        this.submit();
    })
}();
