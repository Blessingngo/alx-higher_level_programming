
document.addEventListener('DOMContentLoaded', function () {
  $(function () {
    $('INPUT#btn_search').click(function () {
      $.ajax({
        type: 'GET',
        url: 'https://www.fourtonfish.com/hellosalut/hello/',
        success: function (data) {
          let input = $('INPUT#language_code;
          if (input) {
            $('DIV#hello').text(Hello);
          }
        }
      });
    });
  });
});
