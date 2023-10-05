$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();

    $.ajax({
      type: 'GET',
      url: `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`,
      dataType: 'json',
      success: function (response) {
        $('#hello').text(response.hello);
      }
    });
  });
});
