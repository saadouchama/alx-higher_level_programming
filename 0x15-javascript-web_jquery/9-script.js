#!/usr/bin/node

$(document).ready(function() {
	$.ajax({
		url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
		method: "GET",
		dataType: "json",
		success: function(data) {
			$("#hello").text(data.hello);
		},
		error: function() {
			$("#hello").text("Failed to fetch translation.");
		}
	});
});
