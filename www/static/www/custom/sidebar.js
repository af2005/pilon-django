const sidebar = function () {
    function toggleCollapsed() {
         $("#sidebar-wrapper").toggleClass("sidebar-collapsed");
        $("#sidebar-collapse-toggle i").toggleClass("bi-chevron-double-left").toggleClass("bi-chevron-double-right");

    }

    function extend() {
        $("#sidebar-wrapper").removeClass("sidebar-collapsed");
        $("#sidebar-collapse-toggle i").addClass("bi-chevron-double-left").removeClass("bi-chevron-double-right");
    }

    function collapse() {
        $("#sidebar-wrapper").addClass("sidebar-collapsed");
        $("#sidebar-collapse-toggle i").removeClass("bi-chevron-double-left").addClass("bi-chevron-double-right");
    }

    function initToggleButton() {
        $("#sidebar-collapse-toggle").click(function () {
            $("#sidebar-wrapper").toggleClass("sidebar-collapsed");
            $("#sidebar-collapse-toggle i").toggleClass("bi-chevron-double-left").toggleClass("bi-chevron-double-right");
        });
    }

    return {
        toggleCollapsed: toggleCollapsed,
        extend: extend,
        collapse: collapse,
        initToggleButton: initToggleButton
    }
}();
document.addEventListener("DOMContentLoaded", function (event) {
    sidebar.initToggleButton();
    $(window).resize(function(e) {
      if($(window).width()<=768){
        sidebar.collapse()
      }
      else{
          sidebar.extend();
      }
    });
});
