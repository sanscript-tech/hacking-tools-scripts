// To Scrape the Amazon Website
const puppeteer = require('puppeteer');
// To print table in the output
const Table = require('cli-table');
const table = new Table({
	head: ['Product Name', 'Price', 'Ratings'],
	colWidths: [140, 10, 10]
})
// To get user arguments
const args = process.argv;
const amazon = (async () => {
	// Launching the browser
	const browser = await puppeteer.launch({ timeout: 0 })
	const page = await browser.newPage()
	await page.goto("https://www.amazon.com/", { timeout: 0, waitUntil: 'domcontentloaded' })
	// Getting the User Input
	const name = args[2]
	// Selecting the Search Box
	const elementHandle = await page.$('input#twotabsearchtextbox.nav-input')
	// Typing in the user argument in the search box
	await elementHandle.type(name)
	// Pressing Enter
	await elementHandle.press('Enter')
	await page.waitForNavigation({waitUntil: "domcontentloaded"})
	const results = await page.evaluate(() => {
		const searchresult = Array.from(document.querySelectorAll('.s-result-item.s-asin'))
		return searchresult.map(r => {
			if (r.querySelector(".a-price")) {
				return {
					product: r.querySelector(".a-color-base.a-text-normal").textContent,
					price: (r.querySelector(".a-price").textContent),
					ratings: r.querySelector(".a-icon-alt") ?  r.querySelector(".a-icon-alt").textContent : "NA"
				};
			}
		}).slice(0,5)
	})
	// Printing the results
	console.log("\nHere are the top 5 products based on your search: \n")
	for(let i=0 ; i<5 ; i++){
		table.push(
			[`${results[i].product}`, `${results[i].price}`, `${results[i].ratings.slice(0, 3)}`]
		)
	}
	console.log(table.toString())
	await browser.close()
})
// Calling the function
if(args.length === 2)
	console.log('Correct Command Usage: `node index.js "product-name"`')
else
	amazon()