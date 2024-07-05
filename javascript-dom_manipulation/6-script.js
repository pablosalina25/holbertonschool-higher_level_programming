// Fetches the character name from the Star Wars API for character ID 5 and updates
// the text content of the element with id 'character' to display the fetched name.

function fetchCharacterNameAndUpdate() {
    fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
       .then(response => response.json())
       .then(data => {
            const characterName = data.name;
            document.getElementById('character').textContent = characterName;
        })
       .catch(error => console.error('Error fetching character data:', error));
}
