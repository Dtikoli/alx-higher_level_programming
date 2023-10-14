$(document).ready(function () {
  $('#btn_translate').on('click', fetchTranslation);

  $('#language_code').on('keypress', function (event) {
    if (event.key === 'Enter') {
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
