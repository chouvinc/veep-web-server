let deleteSet = new Set();

$(".deleteProject").click((e) => {
    let target = $(e.currentTarget);
    let to_delete_id = target.attr('id');

    if (deleteSet.has(to_delete_id)) {
        deleteSet.delete(to_delete_id)
        target.parent().removeClass('deleted');
    } else {
        deleteSet.add(to_delete_id);
        target.parent().addClass('deleted');
    }
});

$(".submitDelete").click((e) => {
    console.log("Submitted")
});