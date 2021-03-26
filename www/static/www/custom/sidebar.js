$(document).ready(function () {


         $(function(){
            $("#menu-toggle").click(function(e) {
                e.preventDefault();
                $("#sidebar-wrapper").toggleClass("toggled");
            });

            $(window).resize(function(e) {
              if($(window).width()<=768){
                $("#sidebar-wrapper").removeClass("toggled");
              }else{
                $("#sidebar-wrapper").addClass("toggled");
              }
            });
          });



});
