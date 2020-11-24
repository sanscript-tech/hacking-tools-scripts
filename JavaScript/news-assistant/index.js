const NewsAPI = require('newsapi');
const prompt = require('prompt-sync')();
// automatically pick platform
const say = require('say')

const api = prompt('Please enter your API key after registering at https://newsapi.org/register : ')
const newsapi = new NewsAPI(api);

// To query top headlines
// All options passed to topHeadlines are optional, but you need to include at least one of them
str = ""
const category = prompt('Please enter the category of news from the following: business, entertainment, general, health, science, sports and technology: ');
newsapi.v2.topHeadlines({
  category: category,
  language: 'en',
  country: 'us'
}).then(response => {
  //if number of rsponses are less than 5, we set l to that number otherwise it's 5
  l = response["articles"].length>5?5:response["articles"].length;
  for (i = 0; i < l; i++) {
  console.log(response["articles"][i]["title"])
  str = str + response["articles"][i]["title"] + ". "
}
say.speak(str)
}
);
