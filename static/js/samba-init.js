$( document ).ready(function() {
  var $item = $('.carousel .item');
  var $wHeight = $(window).height();
  $item.eq(0).addClass('active');
  $item.height($wHeight);
  $item.addClass('full-screen');

  $('.carousel img').each(function() {
    var $src = $(this).attr('src');
    var $color = $(this).attr('data-color');
    $(this).parent().css({
      'background-image' : 'url(' + $src + ')',
      'background-color' : $color
    });
    $(this).remove();
  });

  $(window).on('resize', function (){
    $wHeight = $(window).height();
    $item.height($wHeight);
  });

  $('.carousel').carousel({
    interval: 10000,
    pause: "false"
  });

  $('.navbar-nav a').on('click', function(){
    $('.navbar-collapse').collapse('hide'); //bootstrap 3.x by 3Ecologias
  });

});

//pre-Loader
$(window).on('load', (function() {
		// Animate loader off screen
		$(".se-pre-con").fadeOut("slow");;
	}));

  //jQuery to collapse the navbar on scroll
  $(window).scroll(function() {
      if ($(".navbar").offset().top > 50) {
          $(".navbar-fixed-top").addClass("top-nav-collapse");
      } else {
          $(".navbar-fixed-top").removeClass("top-nav-collapse");
      }
  });

  //jQuery for page scrolling feature - requires jQuery Easing plugin
  $(function() {
      $(document).on('click', 'a.page-scroll', function(event) {
          var $anchor = $(this);
          $('html, body').stop().animate({
              scrollTop: $($anchor.attr('href')).offset().top
          }, 1500, 'easeInOutExpo');
          event.preventDefault();
      });
  });

  // Active Links in Projects
  var selector = '.navbar-right li';

  $(selector).on('click', function(){
      $(selector).removeClass('active');
      $(this).addClass('active');
  });
