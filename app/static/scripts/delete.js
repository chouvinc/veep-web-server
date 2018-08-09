$(".deleteProject").click((e) => {
    console.log($(e.currentTarget).attr('id'));
});

$(".submitDelete").click((e) => {
    console.log("Submitted")
});