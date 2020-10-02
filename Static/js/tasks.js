/* global $ */

// parallax background effect
function Parallax(activate){
    
    if (!activate) return;
    
    $('.parallax').parallax({imageSrc: '/static/galaxy2.jpg'});    
} $(function(){Parallax(true)});



function OnDragStart(event) {
    
    console.log('on drag start');
    
    event
        .dataTransfer
        .setData('text/plain', event.target.id);

}


function OnDragOver(event) {

    console.log('on drag over');
    
    event.preventDefault();
}


function OnDrop(event) {
    
    console.log('on drop');
    
    const id = event
        .dataTransfer
        .getData('text');
        
    console.log(event)
    console.log(event.target)
    
    const draggableElement = document.getElementById(id);
    const dropzone = event.target;
    console.log(draggableElement)  
    dropzone.appendChild(draggableElement);
    
    event
        .dataTransfer
        .clearData();
}