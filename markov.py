import markovify
import tweepy
import random
import datetime
from keys import keys


# Starts the api and auth
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# Creates the post and logs to a file
def generate_post():
    with open('txt/picard.txt') as f:
        text = f.read()

    # Decides if it's late enough for Picard to be drunk
    t = datetime.datetime.now().time()
    start_t = datetime.time(0, 0, 0)
    end_t = datetime.time(2, 0, 0)
    if start_t <= t <= end_t:
        gen_state_size = 1
        text_model = markovify.Text(text, state_size=gen_state_size)
    else:
        gen_state_size = random.randrange(2, 4)
        text_model = markovify.Text(text, state_size=gen_state_size)

    # Create a sentence limited to 140 chars
    if gen_state_size == 1:
        output_text = text_model.make_short_sentence(127) + " #DrunkPicard"
    else:
        output_text = text_model.make_short_sentence(140)

    # Write the status to a file, along with state size
    with open('history.txt', 'a') as f:
        f.write(output_text + '\n')
        f.write('State size of: ')
        f.write(str(gen_state_size) + '\n\n')

    return output_text


# Post the status to Twitter
api.update_status(status=generate_post())
