$(document).ready(function() {
  $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
    $.each(data.results, function(index, movie) {
      $('ul#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});


/*
Alternative: Using .get is correct since data is specified in JSON format in the URL.

$(document).ready(function() {
  $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
    $.each(data.results, function(index, movie) {
      $('<li>').text(movie.title).appendTo('#list_movies');
    });
  });
});
*/
