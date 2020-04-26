$(document).ready(function () {
    $(".scroll").click(function (event) {
        event.preventDefault();
        $('html,body').animate({scrollTop: $(this.hash).offset().top}, 1000);
    });
    $("#slidey").slidey({
        interval: 8000,
        listCount: 5,
        autoplay: false,
        showList: true
    });
    $('.toggle').click(function () {
        // Switches the Icon
        $(this).children('i').toggleClass('fa-pencil');
        // Switches the forms
        $('.form').animate({
            height: "toggle",
            'padding-top': 'toggle',
            'padding-bottom': 'toggle',
            opacity: "toggle"
        }, "slow");
    });
    $(".slidey-list-description").dotdotdot();
    $().UItoTop({easingType: 'easeOutQuart'});
    $(".dropdown").hover(
        function () {
            $('.dropdown-menu', this).stop(true, true).slideDown("fast");
            $(this).toggleClass('open');
        },
        function () {
            $('.dropdown-menu', this).stop(true, true).slideUp("fast");
            $(this).toggleClass('open');
        }
    );

    $(document).ready(function () {
        $("#owl-demo").owlCarousel({
            autoPlay: 3000, //Set AutoPlay to 3 seconds
            items: 3,
            itemsDesktop: [640, 5],
            itemsDesktopSmall: [414, 4]

        });

    });


    var el = document.querySelector('.more');
    var btn = el.querySelector('.more-btn');
    var menu = el.querySelector('.more-menu');
    var visible = false;

    function showMenu(e) {
        e.preventDefault();
        if (!visible) {
            visible = true;
            el.classList.add('show-more-menu');
            menu.setAttribute('aria-hidden', false);
            document.addEventListener('mousedown', hideMenu);
        }
    }

    function hideMenu(e) {

        if(e.target.classList.contains('more-menu-btn')){
            return;
        }

        if (visible) {
            visible = false;
            el.classList.remove('show-more-menu');
            menu.setAttribute('aria-hidden', true);
            document.removeEventListener('mousedown', hideMenu);
        }
    }

    btn.addEventListener('click', (showMenu), false);
});
