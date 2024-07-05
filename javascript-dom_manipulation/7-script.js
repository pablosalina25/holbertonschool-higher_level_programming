// Fetches the titles of all Star Wars movies from the API and updates the 
// element with id 'list_movies' to display each title in a new <li> element.
function fetchMovieTitlesAndUpdate() {
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
      .then(response => response.json())
      .then(data => {
            const movieTitles = data.results.map(movie => movie.title);
            const movieList = document.getElementById('list_movies');
            movieList.innerHTML = '';
            movieTitles.forEach(title => {
                const listItem = document.createElement('li');
                listItem.textContent = title;
                movieList.appendChild(listItem);
            });
        })
      .catch(error => console.error('Error fetching movie data:', error));
}
