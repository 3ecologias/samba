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
    interval: 6000,
    pause: "false"
  });

  $('.nav a').on('click', function(){

    $('.navbar-toggle').click() //bootstrap 3.x by Richard
  });

});

//pre-Loader 
$(window).on('load', (function() {
		// Animate loader off screen
		$(".se-pre-con").fadeOut("slow");;
	}));
