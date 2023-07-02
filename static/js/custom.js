
  (function ($) {
  
  "use strict";

    // MENU
    $('.navbar-collapse a').on('click',function(){
      $(".navbar-collapse").collapse('hide');
    });


    $(window).on('scroll', function(){
      function isScrollIntoView(elem, index) {
        var docViewTop = $(window).scrollTop();
        var docViewBottom = docViewTop + $(window).height();
        var elemTop = $(elem).offset().top;
        var elemBottom = elemTop + $(window).height()*.5;
        if(elemBottom <= docViewBottom && elemTop >= docViewTop) {
          $(elem).addClass('active');
        }
        if(!(elemBottom <= docViewBottom)) {
          $(elem).removeClass('active');
        }
        var MainRoadmapContainer = $('#vertical-scrollable-roadmap')[0];
        var MainRoadmapContainerBottom = MainRoadmapContainer.getBoundingClientRect().bottom - $(window).height()*.5;
        $(MainRoadmapContainer).find('.inner').css('height',MainRoadmapContainerBottom+'px');
      }
      var roadmap = $('#vertical-scrollable-roadmap li');
      Array.from(roadmap).forEach(isScrollIntoView);
    });

  })(window.jQuery);


