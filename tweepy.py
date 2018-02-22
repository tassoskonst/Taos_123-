import json
import tweepy
import string
import re, locale
from collections import Counter
from tweepy import OAuthHandler
def twitter_setup():
    consumer_key = 'mBNndwmOdIFOXt8Vr8tExnEvo'
    consumer_secret ='8eZqWTdVBz7fpj0YplexA0be7BSZJUuGCqww12SOfgw3noi23T'


    access_token = '966369263358496771-5zYcrP7Oj9AUV2hwcPJzLyR2ldZbDQX'
    access_secret = '6khOK5nO3vkWPyZlJN8VBlB0IFlq2Z34h0tFoSxUYwgfW'



    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api=tweepy.API(auth)
    return api



name=input("give me please your Twitter account in quotation marks ")
api=twitter_setup()




extractor = twitter_setup()
tweets = extractor.user_timeline(screen_name=name, count=10)
print("The Number of tweets extracted: {}.\n".format(len(tweets)))
print("the 10 reciest tweets:\n")
for tweet in tweets[:10]:
    print(tweet.text).encode("utf-8")
    print()





file_twitter=open("twitter.txt","w")
file_twitter.write(str(tweets))
file_twitter=open("twitter.txt","r")




frequency = {}
document_text = open('twitter.txt', 'r')
text_string = file_twitter.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print words, frequency[words]
print("the most frequently used word is " + word ),frequency[word]
open("twitter.txt","w").close()