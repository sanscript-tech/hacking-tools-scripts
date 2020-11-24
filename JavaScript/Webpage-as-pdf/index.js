const puppeteer = require('puppeteer');
const args = process.argv;
getTime = () => {
	let today = new Date();
		let y = today.getFullYear();
		let m = today.getMonth() + 1;
		let d = today.getDate();
		let h = today.getHours();
		let mi = today.getMinutes();
		let s = today.getSeconds();
		return y + "-" + m + "-" + d + "-" + h + "-" + mi + "-" + s;
}
// Taking input from the user
if(args.length === 2){
	console.log("Correct command format: `node index.js <webpage-url>`")
}else{
	(async () => {
		// Launching the browser
		const browser = await puppeteer.launch()
		const page = await browser.newPage()
		await page.goto(args[2])
		await page.emulateMediaType('screen')
		// Converting to PDF
		await page.pdf({
			path: `pdf-${getTime()}.pdf`,
			printBackground: true,
			format: 'A4'
		})
		await browser.close()
		console.log("Saved the given webpage as PDF!")
	})();
}