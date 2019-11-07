$(document).ready(function(){
	var baseUrl = 'http://localhost:8000/lista/';
	var filter = $('#filter');
	var filter2 = $('#selectcode');
$(filter).change(function(){
	 	var filter = $(this).val();
	 	console.log(filter);
	 	window.location.href = baseUrl + '?filter=' +filter;
	 });

$(filter2).change(function(){
		var filter2 = $(this).val();
		console.log(filter2);
		window.location.href = baseUrl + '?selectcode=' +filter2;
	});

})

