(function ($) {
$( document ).ready(function() {


  $('.toggle-description-button').on('click', function(e) {
    $('.short-description').toggle();
    $('.long-description').toggle();
  });


});
})(jQuery);
