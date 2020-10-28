import tweepy
import logging
import json
logging.basicConfig(level=logging.INFO)


class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logging.getLogger().info(f"The tweet {tweet.id} is being processed currently")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # These tweets are being ignored for RT as either I am the author or it is a status reply
            return
        # code to favourite the tweet
        if not tweet.favorited:
            try:
                tweet.favorite()
            except Exception as e:
                logging.getLogger().error("There is an error favouriting this tweet", exc_info=True)
        # code to RT the tweet
        if not tweet.retweeted:
            try:
                tweet.retweet()
            except Exception as e:
                logging.getLogger().error("There is an error on favouriting and retweeting", exc_info=True)

    def on_error(self, status):
        logging.getLogger().error(status)

def main(keywords):
    print("Hii! Please enter the credentials for authenticating the API")
    # entering the API credentials
    consumer_key = input("Please enter consumer key ")
    consumer_secret = input("Please enter consumer secret ")
    access_token = input("Please enter access token ")
    access_token_secret = input(" Please enter the access token secret")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        # verifying credentials
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API : ", exc_info=True)
        raise e
    logger.info("API is created sussessfully : ")
    # passing api to FavRetweetListener class
    tweepy.Stream(api.auth, FavRetweetListener(api)).filter(track=keywords, languages=["en"])


if __name__ == "__main__":
    keywords = []
    # Asking user for keyword inputs
    n = int(input("Enter the number of keywords you would base your bot on : "))
    for i in range(n):
        keyword = input("Enter the keyword : ")
        keywords.append(keyword)
    main(keywords)
