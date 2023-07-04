$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();

    var query = $('#query').val();
    var loadingElement = $('#loading');
    var loadingSection = $('#loading-progress');
    var progressMessageElement = $('#progress-msg');
    var progressMessage = "Analyzing your profile...";

    loadingSection.show();
    loadingElement.show();
    progressMessageElement.removeClass('error_msg')
    $('#section_1').addClass('expanded');
    $('#section_2').hide()

    progressMessageElement.text(progressMessage);

    $.ajax({
      url: '/profile',
      type: 'POST',
      data: { 'query': query },
      success: function(response) {
          $.ajax({
            url: "/get_professions",
            type: "GET",
            success: function(response) {
                loadingSection.hide();
                $('#section_1').removeClass('expanded');
                $("#professions").html(response);
                $('#section_2').show()
            },
            error: function(xhr) {
              sendErrorMsg(xhr);
            }
          });
      },
      error: function(xhr) {
          sendErrorMsg(xhr);
        }
    });

    function sendErrorMsg(xhr) {
      var errorMessage = xhr.responseJSON && xhr.responseJSON.error_msg
              ? xhr.responseJSON.error_msg :'Oops! Something went wrong. Please try again.'
      loadingElement.hide();
      progressMessageElement.text(errorMessage).addClass('error_msg');
    }
  });
});
