var status = ""
$('#loader').hide();
$("#save").click(function(d){
    data = {
	name: escape($('iframe').contents().find('html').html()),
	csrftoken: $.cookie('csrftoken')
    }
    console.log(data);
    $('#loader').toggle();
    $.post("gen/_ajax/save_template", data, function(d){
	$('#loader').toggle();
	if(d.status == 'ok'){
	    $("#save").text("saved");
	}
	else {
	    $("#save").text("failed");
	}
    });
});
