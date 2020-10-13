/* global $ */


// $(window).on('load', function(){
//   $('.page').show();
//   $('#loading').hide();
//   $('.preloader').hide();
//   $('.preloader__ring').hide();
//   $('.preloader__sector').hide();
// });


// $(window).on('load', function(){
//   // $('.page').show();
//   // $('#loading').fadeOut(1000);
//   $('.preloader').fadeOut(1000);
//   // $('.preloader__ring').fadeOut(1000);
//   // $('.preloader__sector').fadeOut(1000);
// });


// $(function() {
//     $(window).on('scroll', function() {
//         $('#background').css('margin-top', $(window).scrollTop() * -.3);
//     });
// });




// parallax background effect
function Parallax(){
    
  $('.parallax').parallax({imageSrc: '/static/galaxy3.jpg'});    
    
} $(document).ready(Parallax);