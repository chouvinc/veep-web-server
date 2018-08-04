$('#imRole').change((e) => {
    let selected = $(e.currentTarget).val();
    let roleTypes = 'roleTypes';
    toggleEverythingBut(selected, roleTypes)
});

let toggleEverythingBut = (but, toggleable) => {
    let selectionDiv = $('#' + toggleable);
    selectionDiv.children('p').each((index, val) => {
        let childEl = $(val);
        console.log(childEl)
        if (childEl.attr('id') !== but) {
            childEl.hide();
        }  else {
            childEl.show();
        }
    });
};