$(function () {
  $.get('https://hellosalut.stefanbohacek.com/?lang=fr', function (data) {
    $('div#hello').text(data.hello);
  });
});
