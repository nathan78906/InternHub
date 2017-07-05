var options = {
				valueNames: ['material', 'quantity', 'price', 'deadline']
		}
	, documentTable = new List('mdl-table', options)
	;


$($('th.sort')[0]).trigger('click', function () {
	console.log('clicked');
});

$('input.search').on('keyup', function (e) {
	if (e.keyCode === 27) {
		$(e.currentTarget).val('');
		documentTable.search('');
	}
});