#!/usr/bin/node 

$(document).ready(function() {
	$("#btn_translate").click(function() {
		const languageCode = $("#language_code").val();

		$.ajax({
			url: "https://www.fourtonfish.com/hellosalut/hello/" + languageCode,
			method: "GET",
			dataType: "json",
			success: function(data) {
				$("#hello").text(data.hello);
			},
			error: function() {
				$("#hello").text("Translation not found.");
			}
		});
	});
});
