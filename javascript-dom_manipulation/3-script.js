// Script that toggles the class of the <h1> element between 'red' and 'green' when the user clicks
// on the element with the id 'toggle_header'.
const toggleHeaderElement = document.querySelector('#toggle_header');

toggleHeaderElement.addEventListener('click', function() {
    const headerElement = document.querySelector('h1');
    if (headerElement.classList.contains('red')) {
        headerElement.classList.remove('red');
        headerElement.classList.add('green');
    } else if (headerElement.classList.contains('green')) {
        headerElement.classList.remove('green');
        headerElement.classList.add('red');
    }
});
