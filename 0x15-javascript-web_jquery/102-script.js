$(document).ready(function () {
  $('input#btn_translate').click(function () {
    const lang = $('#language_code').val();
    const fullUrl = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang;
    $.ajax({
      url: fullUrl,
      method: 'GET',
      dataType: 'json'
    })
      .done(function (data) {
        $('div#hello').text(data.hello);
      });
  });
});
