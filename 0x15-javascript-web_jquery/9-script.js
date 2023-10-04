$(document).ready(function() {
  fetch("https://fourtonfish.com/hellosalut/?lang=fr")
    .then(response => response.json())
    .then(data => {
      $('div#hello').text(data.hello);
    });
});


/*
document.addEventListener("DOMContentLoaded", function() {
  fetch("https://fourtonfish.com/hellosalut/?lang=fr")
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      document.querySelector("div#hello").textContent = data.hello;
    });
});


$(document).ready(function() {
  $.getJSON("https://fourtonfish.com/hellosalut/?lang=fr", function(data) {
    $('div#hello').text(data.hello);
  });
});

$(document).ready(function() {
  $.ajax({
    url: "https://fourtonfish.com/hellosalut/?lang=fr",
    type: "GET",
    dataType: "json",
    success: function(data) {
      $('#hello').text(data.hello);
    }
  });
});

*/

