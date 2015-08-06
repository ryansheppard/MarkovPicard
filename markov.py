import markovify
import tweepy

# Opens consumer file
with open('consumerTokens') as f:
    consumer_key = f.readline().strip()
    consumer_secret = f.readline().strip()

# Opens access file
with open('accessTokens') as f:
    access_token = f.readline().strip()
    access_token_secret = f.readline().strip()

# Create auth and api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Read text file
with open('txt/picard.txt') as f:
    text = f.read()

# Create text model. State size 3 for accuracy
text_model = markovify.Text(text, state_size=3)

# Create a sentence limited to 140 chars
output_text = text_model.make_short_sentence(140)

# Post the update to Twitter
api.update_status(status=output_text)
