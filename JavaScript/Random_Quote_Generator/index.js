const quote = document.querySelector(".quote");
const author = document.querySelector(".author");
const btn = document.querySelector("button");
url ="https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=jsonp&jsonp=?";

$('#generate').click(function() {
	$.getJSON(url)
	.done(update)
	.fail(handleError);
});

update = (response) => {
	quote.innerHTML=`${response.quoteText}`;
	author.innerHTML=`- ${response.quoteAuthor}`;
}

handleError = (jqxhr, textStatus, err) => {
	console.log("Request Failed: " + textStatus + ", " + err);
}
	  