
import tweepy

#import the consumer data
from consumer_data import consumer_key, consumer_secret

print("=========================")
print("========= twjnt =========")
print("=========================")


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

print("\n\nAuthentication")
print("--------------\n")

print("Copy the following link to get the permission for your app: ")
print(auth.get_authorization_url())
print("After that, copy your PIN in here: "),
