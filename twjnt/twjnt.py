import tweepy

# import the consumer data
from consumer_data import consumer_key, consumer_secret
import helpers

print("=========================")
print("========= twjnt =========")
print("=========================")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# try first to load already gotten tokens
access_token = helpers.load_access_tokens()

if access_token:
    # if yes, set access token on auth and use the api
    auth.set_access_token(access_token[0], access_token[1])
    api = tweepy.API(auth)

else:
    print("\n\nAuthentication")
    print("--------------\n")

    # if not, ask the user for PIN, save the token for later use and use the api
    print("Copy the following link to get the permission for your app: ")
    print(auth.get_authorization_url())
    pin = input("After that, copy your PIN in here: ")

    try:

        (access_token, access_token_secret) = auth.get_access_token(pin)

        helpers.save_access_tokens(access_token, access_token_secret)

        api = tweepy.API(auth)

    except tweepy.error.TweepError as err:
        print("Could not verify you with a valid PIN.")
        exit()

print("\nLogin successful. Welcome %s! :D\n\n" % api.me().screen_name)
print("What would you like to do?")
