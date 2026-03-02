const readlineSync = require("readline-sync");
const fetch = require("node-fetch");

// api
const api = "https://api.exchangerate-api.com/v4/latest";

// options for currencies
var options = [
	"AED",
	"ARS",
	"AUD",
	"BGN",
	"BRL",
	"CAD",
	"CHF",
	"CLP",
	"CNY",
	"COP",
	"CZK",
	"DKK",
	"EGP",
	"EUR",
	"FJD",
	"GBP",
	"GTQ",
	"HKD",
	"HRK",
	"IDR",
	"HUF",
	"ILS",
	"INR",
	"ISK",
	"JPY",
	"KRW",
	"KZT",
	"MVR",
	"MXN",
	"MYR",
	"NOK",
	"NZD",
	"PAB",
	"PEN",
	"PHP",
	"PKR",
	"PLN",
	"PYG",
	"RON",
	"RUB",
	"SAR",
	"SEK",
	"SGD",
	"THB",
	"TRY",
	"TWD",
	"UAH",
	"UYU",
	"ZAR",
];

console.log("Options available");

// display options
options.forEach(function printOptions(item) {
	console.log(item);
});

var fromCurrency = readlineSync.question("From Currency:");
var fromValue = readlineSync.question("Enter Value:");
var toCurrency = readlineSync.question("To Currency:");
var toValue;

// function to convert
function convert() {
	fetch(`${api}/${fromCurrency}`)
		.then((result) => result.json())
		.then((result) => {
			const rate = result.rates[toCurrency];
            toValue = (fromValue * rate).toFixed(2);
            console.log(`${fromValue} ${fromCurrency} = ${toValue} ${toCurrency}`);
		});
}

convert();
