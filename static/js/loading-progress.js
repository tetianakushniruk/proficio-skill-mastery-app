$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();

    var query = $('#search-bar').val();
    var loadingElement = $('#loading');
    var loadingSection = $('#loading-progress');
    var progressMessageElement = $('#progress-msg');
    var progressMessages = [
      "Checking your input...",
      "Generating a roadmap...",
      "Fetching recommended books...",
      "Loading interview questions...",
      "Preparing tips..."
    ];
    var urls = [
      "/validate",
      "/roadmap",
      "/books",
      "/questions",
      "/tip"
    ];
    var stepCount = progressMessages.length;
    var currentStep = 0;

    loadingSection.show();
    loadingElement.show();
    progressMessageElement.removeClass('error_msg')

    performStep(currentStep);

    function performStep(step) {
      progressMessageElement.text(progressMessages[step]);

      $.ajax({
        url: urls[step],
        type: 'POST',
        data: { query: query },
        success: function(response) {
          if (step < stepCount - 1) {
            performStep(step + 1);
          } else {
            loadingSection.hide();
            $('#section_2').show();
          }
        },
        error: function(xhr) {
          var errorMessage = xhr.responseJSON && xhr.responseJSON.error_msg
              ? xhr.responseJSON.error_msg :'Oops! Something went wrong. Please try again.'
          loadingElement.hide();
          progressMessageElement.text(errorMessage).addClass('error_msg')
        }
      });
    }
  });
});
