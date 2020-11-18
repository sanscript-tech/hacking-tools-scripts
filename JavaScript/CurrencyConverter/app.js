const api="https://api.exchangerate-api.com/v4/latest/USD"
var search=document.querySelector(".search-box");
var date=document.querySelector(".Date");
var from=document.querySelector(".from");
var to=document.querySelector(".to");
var resultFrom;
var resultTo;

from.addEventListener('change', (event) => {
   resultFrom = `${event.target.value}`;
  console.log(resultFrom);
});
to.addEventListener('change', (event) => {
  resultTo = `${event.target.value}`;
 console.log(resultTo);
});
var convert=document.querySelector(".convert");
console.log("working")
var log;
search.addEventListener('input', updateValue);

function updateValue(e) {
  log= e.target.value;
}
convert.addEventListener("click",getResults)
function getResults()
{   
    fetch(`${api}`)
        .then(currency => {
            return currency.json();
          }).then(displayResults);
          

}
function displayResults(currency){
date.innerHTML=currency.date;
let ans=document.querySelector(".ans");
let fromValue=currency.rates[resultFrom];
let toValue=currency.rates[resultTo];
let res=(toValue)/(fromValue);
console.log(log);
ans.innerHTML=res*log;
console.log("working2")
}