$('.header li').mouseenter((e) => {
    let parentListItem = $(e.currentTarget).parent();
    parentListItem.addClass('selected');
});

$('.header li').mouseleave((e) => {
    let parentListItem = $(e.currentTarget).parent();
    parentListItem.removeClass('selected');
});