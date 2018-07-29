$('.header a').mouseenter((e) => {
    let parentListItem = $(e.currentTarget).parent();
    parentListItem.addClass('selected');
});

$('.header a').mouseleave((e) => {
    let parentListItem = $(e.currentTarget).parent();
    parentListItem.removeClass('selected');
});