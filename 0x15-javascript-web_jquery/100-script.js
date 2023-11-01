#!/usr/bin/node

document.addEventListener("DOMContentLoaded", function() {

	const header = document.querySelector('header');

	if (header) {
		header.style.color = '#FF0000';
	} else {
		console.log("Header element not found.");
	}
});
