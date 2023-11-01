$(document).ready(function () {
  $('#add_item').click(function () {
    const item = $('<li>Item</li>');
    // using just item = "<li>Item</li>" will work here but
    // it won't be a jQuery object, so you won't have the full range
    // of jQuery methods available for further manipulation
    // for example item.addClass('newclass') wiil not work
    $('ul.my_list').append(item);
  });
});
