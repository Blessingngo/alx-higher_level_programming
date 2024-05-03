document.addEventListener('DOMContentLoaded', function () {
  $(function () {
    $('INPUT#btn_search').click(function () {
      $.ajax({
        type: 'GET',
        url: 'https://www.fourtonfish.com/hellosalut/hello/',
        success: function (data) {
          let input = $('INPUT#language_code').val();
          if (input) {
            $('INPUT#btn_translate').text(data.query.results.channel.wind.speed);
          }
        }
      });
    });

    $('INPUT#language_code').keypress(function (e) {
      if (e.which === 13) {
        $('INPUT#btn_search').click();
      }
    });
  });
});
