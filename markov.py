import markovify
import tweepy


with open('consumerTokens') as f:
    consumer_key = f.readline().strip()
    consumer_secret = f.readline().strip()

with open('accessTokens') as f:
    access_token = f.readline().strip()
    access_token_secret = f.readline().strip()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.me()

with open('txt/picard.txt') as f:
    text = f.read()

text_model = markovify.Text(text, state_size=3)

output_text = text_model.make_short_sentence(140)

api.update_status(status=output_text)
