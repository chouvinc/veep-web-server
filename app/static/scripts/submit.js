$('p[class="submit_type"] > select').change((e) => {
    showSelectedForms(e.currentTarget.value);
});

function showSelectedForms (selectedValue) {
    $('#selections').children().each((index, element) => {
        if ($(element).attr('id') === selectedValue) {
            $(element).show();
        } else {
            $(element).hide();
        }
    });
}