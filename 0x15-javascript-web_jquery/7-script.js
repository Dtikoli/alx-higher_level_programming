$(document).ready(function() {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    type: "GET",
    dataType: "json"
  }).done(function(data) {
    $('DIV#character').text(data.name);
  });
});
