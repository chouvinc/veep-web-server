$('#apply').mouseenter((e) => {
    $(e.currentTarget).addClass('selected');
});

$('#apply').mouseleave((e) => {
    $(e.currentTarget).removeClass('selected');
});