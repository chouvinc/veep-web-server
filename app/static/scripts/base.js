$('.header li').mouseenter((e) => {
    $(e.currentTarget).addClass('selected');
});

$('.header li').mouseleave((e) => {
    $(e.currentTarget).removeClass('selected');
});