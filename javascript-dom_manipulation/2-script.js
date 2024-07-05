// Script that adds the class 'red' to the <h1> element when the user clicks
// on the element with the id 'red_header'.
const redHeaderElement = document.querySelector('#red_header');

redHeaderElement.addEventListener('click', function() {
    const headerElement = document.querySelector('h1');
    headerElement.classList.add('red');
});
