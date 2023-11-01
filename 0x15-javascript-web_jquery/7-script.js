$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  fetch(url)
    .then(response => {
      if (response.ok) {
        return response.json();
      }
    })
    .then(data => {
      const name = data.name;
      $('div#character').text(name);
    });
});
