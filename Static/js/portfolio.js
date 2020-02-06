/* global $ */

// typewriter function:
function Typewriter(input) {
    
    // exit if end of text has been reached:
    if (input.text_position==input.full_text.length+1) return;
    
    // update inner html:
    input.destination.innerHTML = input.full_text.substring(0, input.text_position);
    
    // increment text position to next character:
    input.text_position++
} 



// wrapper function for executing typewiter:
function ExecuteTypwriter(activate) {

    // exit if active is set to false:
    if (!activate) return;

    // initialize inputs:
    var projects__text_header = {
        'destination' : document.getElementById('projects--text-header'),
        'full_text' : document.getElementById('projects--text-header').innerHTML,
        'partial_text' : '',
        'text_position' : 0,
    }
    
    var projects__text_details__icardio_title = {
        'destination' : document.getElementById('projects--text-details--icardio-title'),
        'full_text' : document.getElementById('projects--text-details--icardio-title').innerHTML,
        'partial_text' : '',
        'text_position' : 0,
    }
    
    var projects__text_details__icardio_line_1 = {
        'destination' : document.getElementById('projects--text-details--icardio-line-1'),
        'full_text' : document.getElementById('projects--text-details--icardio-line-1').innerHTML,
        'partial_text' : '',
        'text_position' : 0,
    }
    
    var projects__text_details__airplant_title = {
        'destination' : document.getElementById('projects--text-details--airplant-title'),
        'full_text' : document.getElementById('projects--text-details--airplant-title').innerHTML,
        'partial_text' : '',
        'text_position' : 0,
    }
    
    var projects__text_details__airplant_line_1 = {
        'destination' : document.getElementById('projects--text-details--airplant-line-1'),
        'full_text' : document.getElementById('projects--text-details--airplant-line-1').innerHTML,
        'partial_text' : '',
        'text_position' : 0,
    }
    
    var projects__text_details__airplant_line_2 = {
        'destination' : document.getElementById('projects--text-details--airplant-line-2'),
        'full_text' : document.getElementById('projects--text-details--airplant-line-2').innerHTML,
        'partial_text' : '',
        'text_position' : 0,
    }
    
    var projects__text_details__airplant_line_3 = {
        'destination' : document.getElementById('projects--text-details--airplant-line-3'),
        'full_text' : document.getElementById('projects--text-details--airplant-line-3').innerHTML,
        'partial_text' : '',
        'text_position' : 0,
    }
    
    var projects__text_details__airplant_line_4 = {
        'destination' : document.getElementById('projects--text-details--airplant-line-4'),
        'full_text' : document.getElementById('projects--text-details--airplant-line-4').innerHTML,
        'partial_text' : '',
        'text_position' : 0,
    }
    
    var artwork__text_header = {
        'destination' : document.getElementById('artwork--text-header'),
        'full_text' : document.getElementById('artwork--text-header').innerHTML,
        'partial_text' : '',
        'text_position' : 0,
    }
    
    var contact__text_header = {
        'destination' : document.getElementById('contact--text-header'),
        'full_text' : document.getElementById('contact--text-header').innerHTML,
        'partial_text' : '',
        'text_position' : 0,
    }
    
    // set interval for typewriter function for header:
    setInterval(function() {Typewriter(projects__text_header);}, 2300/projects__text_header.full_text.length); 
    setInterval(function() {Typewriter(projects__text_details__icardio_title);}, 2800/projects__text_details__icardio_title.full_text.length);
    setInterval(function() {Typewriter(projects__text_details__icardio_line_1);}, 2700/projects__text_details__icardio_line_1.full_text.length);
    setInterval(function() {Typewriter(projects__text_details__airplant_title);}, 2000/projects__text_details__airplant_title.full_text.length);
    setInterval(function() {Typewriter(projects__text_details__airplant_line_1);}, 2700/projects__text_details__airplant_line_1.full_text.length);
    setInterval(function() {Typewriter(projects__text_details__airplant_line_2);}, 2500/projects__text_details__airplant_line_2.full_text.length);
    setInterval(function() {Typewriter(projects__text_details__airplant_line_3);}, 2100/projects__text_details__airplant_line_3.full_text.length);
    setInterval(function() {Typewriter(projects__text_details__airplant_line_4);}, 2900/projects__text_details__airplant_line_4.full_text.length);
    setInterval(function() {Typewriter(artwork__text_header);}, 2400/artwork__text_header.full_text.length);
    setInterval(function() {Typewriter(contact__text_header);}, 2200/contact__text_header.full_text.length);
} ExecuteTypwriter(true);