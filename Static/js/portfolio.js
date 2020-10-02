/* global $ */


// carousel function:
function ExecuteCarousel(activate) {

    // exit if active is set to false:
    if (!activate) return;
    
    $(document).ready(function(){
        
        $('#artwork--image').slick({
            autoplay: true,
            autoplaySpeed: 3000,
            infinite: true,
            speed: 2000,
            fade: true,
            cssEase: 'linear',
            prevArrow:'',
            nextArrow:'',
            dots: true,
            centerMode: true,
        });
    });

} $(function(){ExecuteCarousel(true)});



// typewriter function:
function Typewriter(input) {
    
    if (!isScrolledIntoView(input.destination)) return;
    
    // exit if end of text has been reached:
    if (input.text_position==input.full_text.length+1) return;
    
    // update inner html:
    input.destination.innerHTML = input.full_text.substring(0, input.text_position);
    
    // increment text position to next character:
    input.text_position++;
} 



// checks if element is in view:
function isScrolledIntoView(elem) {
    
    var docViewTop = $(window).scrollTop();
    var docViewBottom = docViewTop + $(window).height();
    var elemTop = $(elem).offset().top;
    var elemBottom = elemTop + $(elem).height();

    return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
}



// wrapper function for executing typewriter:
function ExecuteTypwriter(activate) {

    // exit if active is set to false:
    if (!activate) return;

    // initialize inputs:
    var typewriter_inputs = {};
    var element_id_list = {
        projects__text_header : 'projects--text-header', 
        artwork__text_header : 'artwork--text-header',
        contact__text_header : 'contact--text-header',
        projects__credentials_header : 'credentials--text-header',
    };
    
    // create input objects:
    for (var element_id in element_id_list) {
        
        typewriter_inputs[element_id] = {
            destination : document.getElementById(element_id_list[element_id]),
            full_text : document.getElementById(element_id_list[element_id]).innerHTML,
            partial_text : '',
            text_position : 0,
        };
    }
    
    // set interval for typewriter function for header:
    setInterval(function() {Typewriter(typewriter_inputs.projects__text_header);}, 2300/typewriter_inputs.projects__text_header.full_text.length); 
    setInterval(function() {Typewriter(typewriter_inputs.artwork__text_header);}, 2400/typewriter_inputs.artwork__text_header.full_text.length);
    setInterval(function() {Typewriter(typewriter_inputs.contact__text_header);}, 2100/typewriter_inputs.contact__text_header.full_text.length);
    setInterval(function() {Typewriter(typewriter_inputs.projects__credentials_header);}, 2100/typewriter_inputs.projects__credentials_header.full_text.length);
} $(function(){ExecuteTypwriter(true)});



// parallax background effect
function Parallax(activate){
    
    if (!activate) return;
    
    $('.parallax').parallax({imageSrc: '/static/galaxy3.jpg'});    
} $(function(){Parallax(true)});
