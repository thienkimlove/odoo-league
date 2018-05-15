
(function($){
 jQuery(document).ready(function(){
  $("#scroll-wrapper").click(function() {
            //alert("hnfghdfsgfd");
            $('html, body').animate({
              scrollTop: $("#homepage").offset().top
            }, 1000);
          });
});
})(jQuery);

(function($){
 jQuery(document).ready(function(){
  $("#scroll-wrapper3").click(function() {
            //alert("hnfghdfsgfd");
            $('html, body').animate({
              scrollTop: $("#features").offset().top
            }, 1000);
          });
});
})(jQuery);


    // scroll-to-top button show and hide
    jQuery(document).ready(function(){
      jQuery(window).scroll(function(){
        if (jQuery(this).scrollTop() > 100) {
          jQuery('.scrollup').fadeIn();
        } else {
          jQuery('.scrollup').fadeOut();
        }
      });
    // scroll-to-top animate
    jQuery('.scrollup').click(function(){
      jQuery("html, body").animate({ scrollTop: 0 }, 600);
      return false;
    });


  });

(function($){
    jQuery(document).ready(function() {

       $('#brands-carousel').owlCarousel({
            margin: 10,
            nav: true,
            loop: true,
            dots:false,
            responsiveClass:true,
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 3
                },
                1000: {
                    items: 5
                }
            }
        });

        $('#clubs-carousel').owlCarousel({
            margin: 10,
            nav: true,
            loop: true,
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items:4
                },
                1000: {
                    items: 8,
                    nav:false
                }
            }
        });

        $('#matchweek-carousel').owlCarousel({
            margin: 10,
            nav: true,
            loop: true,
            dots:false,
            responsiveClass:true,
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 2
                },
                991: {
                    items: 3
                },
                1000: {
                    items: 4,
                }
            }
        });

        $('#news-carousel').owlCarousel({
            margin: 0,
            nav: true,
            loop: true,
            nav:false,
            responsiveClass:true,
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items:1
                },
                1000: {
                    items: 1
                }
            }
        });


        $('#news02-carousel').owlCarousel({
            margin: 20,
            loop: true,
            nav:false,
            dots:false,
            responsiveClass:true,
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 2
                },
                1000: {
                    items: 3
                }
            }
        });


        $('#news03-carousel').owlCarousel({
            margin: 20,
            loop: true,
            nav:false,
            rows: true,
            rowsCount: 2,
            responsiveClass:true,
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 2
                },
                1000: {
                    items: 2
                }
            }
        });

        $('#matchweek-carousel02').owlCarousel({
            margin: 10,
            nav: true,
            loop: true,
            dots:false,
            responsiveClass:true,
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 2
                },
                991: {
                    items: 3
                },
                1000: {
                    items: 4,
                }
            }
        });
    });
})(jQuery);



    
     
