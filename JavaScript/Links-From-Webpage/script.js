// select all the <a> tags
var selectTag = document.querySelectorAll("a");
// an array to store the title of the link and the link
var array = [];
for (var i = 0; i < selectTag.length; i++) {
	var text = selectTag[i].textContent;
	var text = text.replace(/\s+/g, " ").trim();
	var link = selectTag[i].href;
	array.push([text, link]);
}
// Function to create the table with title and link
function make_table() {
	// table to store the data
	var table = "<table><thead><th>Name</th><th>Links</th></thead><tbody>";
	for (var i = 0; i < array.length; i++) {
		table +=
			"<tr><td>" + array[i][0] + "</td><td>" + array[i][1] + "</td></tr>";
	}
	var w = window.open("");
	// displays the table in a new window
	w.document.write(table);
}
make_table();
