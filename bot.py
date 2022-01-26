import json
from twython import Twython
import garkov

#load keys into array
keys = json.loads(open('keys.json').read())

#call garkov.py to get a new comic to post
garkov.GetComic()

#authenticate to twitter using Twython
APP_KEY = keys["api_key"]
APP_SECRET = keys["api_key_secret"]
ACCESS_TOKEN = keys["access_token"]
ACCESS_SECRET = keys["access_secret"]

bot = Twython(APP_KEY,APP_SECRET,ACCESS_TOKEN,ACCESS_SECRET)

photo = open('garkov.jpg', 'rb')
response = bot.upload_media(media=photo)
bot.update_status(status='', media_ids=[response['media_id']])