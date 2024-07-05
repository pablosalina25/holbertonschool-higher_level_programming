// a JavaScript script that updates the text color of the header element to red (#FF0000)
// when the user clicks on the tag with id red_header:

const headerelent = document.querySelector('red_header');
headerelent.addEventListener('click', function() {
    var headerElement = document.querySelector('h1');
    headerElement.style.color = "#FF0000";
});