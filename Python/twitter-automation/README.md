# Twitter automation
- - - - - - - - 
This is a Twitter script that can automatically like and retweet tweets containing user-specified keywords.</br>
This bot uses the Tweepy stream to actively watch for tweets that contain certain keywords. For each tweet, if you’re not the tweet author, it will mark the tweet as Liked and then retweet it.

## Requirements
```pip install tweepy```</br>

## Setting up the twitter API
- Go to the [Twitter Developer's site](dev.twitter.com) and sign in with the Twitter account you want to associate with your app.
- After logging in, click on the downwards arrow next to your image and select "My Applications". This is where all your registered Twitter Apps will be shown.
- Create your application by clicking on the 'Create a new application' button.
- Fill in the relevant details in the application form, including your website URL in the website field. This is where your app will be hosted. The Callback URL field can be ignored for the time being. Read and accept the terms and conditions and click on "Create Your Twitter Application" button and you're good to go!
- You will be taken to a new screen where you need to create an access token for yourself to authorize your Twitter app for your Twitter account. Click on "Create my access token" to do this. Note: You will need to generate a new token if you change app permissions at any future point of time. 
- After the token is generated, choose the type of access you require. Change it to 'read and write' to give the app permission to follow other accounts on your behalf. This will prompt a mobile verification with your twitter account.
- You are done setting up your Twitter API. Keep a note of the following (which are to be kept secret):
    - Consumer Key
    - Consumer Secret
    - OAuth Access Token
    - OAuth Access Token Secret

## To use
Run ```python tweet.py```</br>
Specify the credentials as asked</br>
Enter the number of keywords you would like to base your search on</br>
Enter the names of keywords</br>
And the bot will start it's job!


## Example Tweets

I used this script to RT tweets with ```python``` keyword

![alt-text](https://github.com/TaniaMalhotra/hacking-tools-scripts/blob/twitter-automation/Python/twitter-automation/images/Screenshot%20(476)_LI.jpg)
