#!/usr/bin/node

$(document).ready(function() {
	$.ajax({
	url: "https://swapi-api.alx-tools.com/api/films/?format=json",
	method: "GET",
	dataType: "json",
	success: function(data) {
		$.each(data.results, function(index, movie) {
			$("#list_movies").append("<li>" + movie.title + "</li>");
		});
	},
	error: function() {
		$("#list_movies").append("<li>Failed to fetch movie titles.</li>");
	}
	});
});
