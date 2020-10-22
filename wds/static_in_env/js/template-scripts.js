jQuery(document).ready(function($) {
    // Owl Carousel                     
    var owl = $('.carousel-default');
    owl.owlCarousel({
        nav: true,
        dots: true,
        items: 1,
        loop: true,
        navText: ["&#xe605", "&#xe606"],
        autoplay: true,
        autoplayTimeout: 5000
    });

    // Owl Carousel - Content Blocks  
    var owl = $('.carousel-blocks');
    owl.owlCarousel({
        nav: true,
        dots: false,
        items: 4,
        responsive: {
            0: {
                items: 1
            },
            481: {
                items: 3
            },
            769: {
                items: 4
            }
        },
        loop: true,
        navText: ["&#xe605", "&#xe606"],
        autoplay: true,
        autoplayTimeout: 5000
    });

    // Owl Carousel - Content 3 Blocks
    var owl = $('.carousel-3-blocks');
    owl.owlCarousel({
        nav: true,
        dots: true,
        items: 3,
        responsive: {
            0: {
                items: 1
            },
            481: {
                items: 2
            },
            769: {
                items: 3
            }
        },
        loop: true,
        navText: ["&#xe605", "&#xe606"],
        autoplay: true,
        autoplayTimeout: 5000
    });

    var owl = $('.carousel-fade-transition');
    owl.owlCarousel({
        nav: true,
        dots: true,
        items: 1,
        loop: true,
        navText: ["&#xe605", "&#xe606"],
        autoplay: true,
        animateOut: 'fadeOut',
        autoplayTimeout: 5000
    });

    // skillbar
    $('.skillbar').bind('inview', function(event, visible) {
        if (visible) {
            $('.skillbar').each(function() {
                $(this).find('.skillbar-bar').animate({
                    width: $(this).attr('data-percent')
                }, 3000);
            });

        }
    });

    // Simple Preloader
    $(window).load(function() {
        $("#page-overlay").delay(200).fadeOut("slow");
    })

    // countTo
    $('.timer').bind('inview', function(event, visible) {
        if (visible) {
            $('.timer').countTo({
                speed: 1400,
                refreshInterval: 10,
                formatter: function(value, options) {
                    return value.toFixed(options.decimals);
                },
                onUpdate: function(value) {
                    console.debug(this);
                },
                onComplete: function(value) {
                    console.debug(this);
                }
            });
            $(this).off(event);
        }
    });

    function count(options) {
        var $this = $(this);
        options = $.extend({}, options || {}, $this.data('countToOptions') || {});
        $this.countTo(options);
    }
    // custom formatting example
    $('#decimal').data('countToOptions', {
        formatter: function(value, options) {
            return value.toFixed(options.decimals).replace(/\B(?=(?:\d{3})+(?!\d))/g, ',');
        }
    });

    // Sticky Nav Bar
    $(window).scroll(function() {
        if ($(this).scrollTop() > 20) {
            $('.sticky').addClass("fixed");
        } else {
            $('.sticky').removeClass("fixed");
        }
    });

    // Lightbox
    $('a[data-rel^=lightcase]').lightcase({
        maxWidth: 1000,
        maxHeight: 'auto',
        transition: 'scrollHorizontal',
        speedIn: 600,
        speedOut: 600,
        video: {
            width: 1000,
            height: 'auto',
            loop: true
        },
    });

    // Content Animation
    $.fn.isInViewport = function() {
        var elementTop = $(this).offset().top;
        var elementBottom = elementTop + $(this).outerHeight();

        var viewportTop = $(window).scrollTop();
        var viewportBottom = viewportTop + $(window).height();

        return elementBottom > viewportTop && elementTop < viewportBottom;
    };

    $(window).on('resize scroll', function() {
        $('.animated-element').each(function() {
            if ($(this).isInViewport()) {
                $(this).addClass('animation');
            }
        });
    });

    // Custom scripts
    // Pie Charts 
    $('.chart').bind('inview', function(event, visible) {
        if (visible) {
            $('.chart').easyPieChart({
                barColor: '#28a5df',
                trackColor: '',
                size: 127,
                lineWidth: 2,
                scaleLength: 0,
                animate: {
                    duration: 8000,
                    enabled: true
                }
            });
        }
    });
});


// In view animation
/**
 * author Remy Sharp
 * url http://remysharp.com/2009/01/26/element-in-view-event-plugin/
 */
(function($) {
    function getViewportHeight() {
        var height = window.innerHeight; // Safari, Opera
        var mode = document.compatMode;

        if ((mode || !$.support.boxModel)) { // IE, Gecko
            height = (mode == 'CSS1Compat') ?
                document.documentElement.clientHeight : // Standards
                document.body.clientHeight; // Quirks
        }

        return height;
    }

    $(window).scroll(function() {
        var vpH = getViewportHeight(),
            scrolltop = (document.documentElement.scrollTop ?
                document.documentElement.scrollTop :
                document.body.scrollTop),
            elems = [];

        // naughty, but this is how it knows which elements to check for
        $.each($.cache, function() {
            if (this.events && this.events.inview) {
                elems.push(this.handle.elem);
            }
        });

        if (elems.length) {
            $(elems).each(function() {
                var $el = $(this),
                    top = $el.offset().top,
                    height = $el.height(),
                    inview = $el.data('inview') || false;

                if (scrolltop > (top + height) || scrolltop + vpH < top) {
                    if (inview) {
                        $el.data('inview', false);
                        $el.trigger('inview', [false]);
                    }
                } else if (scrolltop < (top + height)) {
                    if (!inview) {
                        $el.data('inview', true);
                        $el.trigger('inview', [true]);
                    }
                }
            });
        }
    });

    // kick the event to pick up any elements already in view.
    // note however, this only works if the plugin is included after the elements are bound to 'inview'
    $(function() {
        $(window).scroll();
    });
})(jQuery);