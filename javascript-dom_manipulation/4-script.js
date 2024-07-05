// Adds a new <li> to the list when the user clicks on the element with id 'add_item'.
const addItemButton = document.querySelector('#add_item');

addItemButton.addEventListener('click', function() {
    const newItem = document.createElement('li');
    newItem.textContent = "Item";
    const myList = document.querySelector('.my_list');
    myList.appendChild(newItem);
});
