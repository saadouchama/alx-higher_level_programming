#!/usr/bin/node

$(document).ready(function() {
	$("#add_item").click(function() {
		const newItem = $("<li>Item</li>");
		$(".my_list").append(newItem);
	});
});
