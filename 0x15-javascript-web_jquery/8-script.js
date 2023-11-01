$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  fetch(url)
    .then(response => {
      if (response.ok) {
        return response.json();
      }
    })
    .then(data => {
      const results = data.results;
      for (const obj of results) {
        const title = obj.title;
        const list = $('<li></li>').text(title);
        $('ul#list_movies').append(list);
      }
    });
});
