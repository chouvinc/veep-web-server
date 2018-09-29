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
    // TODO: move string constants to a separate file
    let dataType =  window.location.pathname.replace('admin/delete/', '');
    let fullUrl = window.location.href;
    let json = JSON.stringify({"type": dataType.substring(1, dataType.length), "ids": Array.from(deleteSet)});

    console.log(Array.from(deleteSet));
    $.ajax({
        type: 'POST',
        url: fullUrl,
        dataType: 'json',
        contentType: 'application/json',
        data: json,
        success: function (data) {
            if (data.redirect) {
                console.log(data.redirect);
                window.location.href = data.redirect;
            }
        }
    });
});
