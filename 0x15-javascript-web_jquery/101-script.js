$(document).ready(function () {
  $('div#add_item').click(function () {
    const item = $('<li>Item</li>');
    $('ul.my_list').append(item);
  });

  $('div#remove_item').click(function () {
    $('ul.my_list li:last').remove();
  });

  $('div#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
