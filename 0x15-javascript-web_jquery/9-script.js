$(document).ready(function () {
  // using $(document).ready(function (){}) ensure that the code
  // within the function is executed after the DOM is fully loaded
  // because if javascript code run before DOM is available and try to interact
  // with DOM elements that can lead to issues
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  fetch(url)
    .then(response => {
      if (response.ok) {
        return response.json();
      }
    })
    .then(data => {
      const translation = data.hello;

      $('div#hello').text(translation);
    });
});
