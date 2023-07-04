$(document).ready(function() {
  $(document).on('click', '.suggested-profession', function(event) {
    event.preventDefault();

    var profession = $(this).data('profession');
    window.location.href = '/?query=' + encodeURIComponent(profession);
  });
});
