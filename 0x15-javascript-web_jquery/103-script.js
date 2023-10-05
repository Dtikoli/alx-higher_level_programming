$(document).ready(function () {
  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (even) {
    if (even.which === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation () {
    const languageCode = $('#language_code').val();

    $.ajax({
      type: 'GET',
      url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
      dataType: 'json',
      success: function (response) {
        $('#hello').text(response.hello);
      }
    });
  }
});
