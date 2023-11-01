#!/usr/bin/node

$(document).ready(function() {
	$("#btn_translate").click(fetchTranslation);
	$("#language_code").keypress(function(event) {
		if (event.which === 13) {
			fetchTranslation();
		}
	});

	function fetchTranslation() {
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
	}
});
