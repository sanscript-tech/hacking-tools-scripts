const Wappalyzer = require('wappalyzer');
const Table = require('cli-table')
const args = process.argv
const url = args[2]
// Table to print the output
const table = new Table({
	head: ['Name', 'Confidence', 'Website', 'Category']
})
const options = {
	debug: false,
	delay: 500,
	headers: {},
	maxDepth: 3,
	maxUrls: 10,
	maxWait: 5000,
	recursive: true,
	probe: true,
	userAgent: 'Wappalyzer',
	htmlMaxCols: 2000,
	htmlMaxRows: 2000,
};
;(async function() {
	const wappalyzer = await new Wappalyzer(options)
	try{
		await wappalyzer.init()
		const headers = {}
		const site = await wappalyzer.open(url, headers)
		site.on('error', console.error)
		const results = await site.analyze()
		for(var i=0 ; i<results.technologies.length ; i++){
			table.push([`${results.technologies[i].name}`, `${results.technologies[i].confidence}`, `${results.technologies[i].website}`, `${results.technologies[i].categories[0].name}`])
		}
		console.log(table.toString())
	}catch (error) {
		console.error(error)
	}
	await wappalyzer.destroy()
})()