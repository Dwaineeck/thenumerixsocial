$(document).ready(function(){
    $(".badge-pill").click(function(){
        $(this).siblings(".details").slideToggle();
    });
});