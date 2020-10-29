# Twitter automation
- - - - - - - - 
This is a Twitter script that can automatically like and retweet tweets containing user-specified keywords.</br>
This bot uses the Tweepy stream to actively watch for tweets that contain certain keywords. For each tweet, if you’re not the tweet author, it will mark the tweet as Liked and then retweet it.

## Requirements
```pip install tweepy```</br>

## Setting up the twitter API
- Go to the [Twitter Developer's site](dev.twitter.com) and sign in with the Twitter account you want to associate with your app and click on ```apply```.

![alt-text](https://github.com/TaniaMalhotra/hacking-tools-scripts/blob/twitter-automation/Python/twitter-automation/images/open_dev_link.png)

- Fill the application form using relevant details


![alt-text](https://github.com/TaniaMalhotra/hacking-tools-scripts/blob/twitter-automation/Python/twitter-automation/images/apply_to_make_a_bot.png)

![alt-text](https://github.com/TaniaMalhotra/hacking-tools-scripts/blob/twitter-automation/Python/twitter-automation/images/enter_info.png)


- You'll get a message as shown; after which you're required to confirm your email

![alt-text](https://github.com/TaniaMalhotra/hacking-tools-scripts/blob/twitter-automation/Python/twitter-automation/images/confirm_email.png)



- Enter the name of the bot and click on ```get keys```

![alt-text](https://github.com/TaniaMalhotra/hacking-tools-scripts/blob/twitter-automation/Python/twitter-automation/images/enter_app_name.png)


- Click on skip to dashboard

![alt-text](https://github.com/TaniaMalhotra/hacking-tools-scripts/blob/twitter-automation/Python/twitter-automation/images/skip%20to%20dashboard.jpg)


- Edit your app permissions and set it to ```READ AND WRITE```

![alt-text](https://github.com/TaniaMalhotra/hacking-tools-scripts/blob/twitter-automation/Python/twitter-automation/images/edit_app_permissions.png)

- Click on ```KEYS AND TOKENS``` to see your API keys.

![alt-text](https://github.com/TaniaMalhotra/hacking-tools-scripts/blob/twitter-automation/Python/twitter-automation/images/keys.png)

- You are done setting up your Twitter API. Keep a note of the following (which are to be kept secret):
    - Consumer Key
    - Consumer Secret
    - API Key
    - API Secret

## To use
Run ```python tweet.py```</br>
Specify the credentials as asked</br>
Enter the number of keywords you would like to base your search on</br>
Enter the names of keywords</br>
And the bot will start it's job!


## Example Tweets

I used this script to RT tweets with ```python``` keyword

![alt-text](https://github.com/TaniaMalhotra/hacking-tools-scripts/blob/twitter-automation/Python/twitter-automation/images/Screenshot%20(476)_LI.jpg)
