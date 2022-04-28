import os
import io
import tweepy
import keys_zhangyu as keys
import json
import requests

consumer_key = keys.consumer_key
consumer_secret= keys.consumer_secret
access_token = keys.access_token
access_token_secret = keys.access_token_secret
bearer_token = keys.bearer_token

# define the local location of files
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read_txt(file_name):

    # load file
    file = open(os.path.join(__location__, file_name),encoding='utf-8-sig')

    source_reply = {}
    index = 1
    with io.open(os.path.join(__location__, file_name), 'r',encoding='utf-8') as lines:
        for line in lines:
            line = line[:-2]
            sequence = line.split(',')
            source_reply[index] = sequence
            index +=1 
    return source_reply

# train_set_idx = read_txt('train.data.txt')
# dev_set_idx = read_txt('dev.data.txt')
# test_set_idx = read_txt('test.data.txt')

# auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
# auth.set_access_token(access_token,access_token_secret)
# api = tweepy.API(auth)

client = tweepy.Client(bearer_token, consumer_key= consumer_key,consumer_secret= consumer_secret,access_token= access_token,access_token_secret= access_token_secret, wait_on_rate_limit= True)
api = tweepy.API(client)

def find_tweet_byID(ID):
    tweets = client.get_tweets(
        ids= ID,
        expansions=["attachments.poll_ids", "attachments.media_keys", "author_id", "entities.mentions.username", "geo.place_id", "in_reply_to_user_id", "referenced_tweets.id", "referenced_tweets.id.author_id"],
        media_fields=["duration_ms","height","media_key","preview_image_url","type","url","width","public_metrics","non_public_metrics","organic_metrics","promoted_metrics","alt_text"],
        place_fields = ["contained_within","country","country_code","full_name","geo","id","name","place_type"],
        poll_fields = ["duration_minutes", "end_datetime", "id", "options", "voting_status"],
        tweet_fields = ["attachments", "author_id", "context_annotations", "conversation_id", "created_at", "entities", "geo", "id", "in_reply_to_user_id", "lang", "non_public_metrics", "public_metrics", "organic_metrics", "promoted_metrics", "possibly_sensitive", "referenced_tweets", "reply_settings", "source", "text", "withheld"],
        user_fields = ["created_at", "description", "entities", "id", "location", "name", "pinned_tweet_id", "profile_image_url", "protected", "public_metrics", "url", "username", "verified", "withheld"],
        user_auth=True
    )
    return tweets

data1 = find_tweet_byID(['1281343950956171265'])
print(data1)

user_dict = {   "screen_name":"",
                "name":"",
                "id":"",
                "id_str":"",
                "indices": [],
}


sampleDict = { "created_at": "NA", 
                "id": "",
                "id_str": "",
                "text": "",
                "truncated": False,
                "entities":{
                    "hashtags": [],
                    "symbols": [],
                    "user_mentions":[
                        {

                        }
                    ]
                }
                 }

with open("387030572779847680.json", "w") as write_file:
    json.dump(sampleDict, write_file, indent=4)

# data2 = find_tweet_byID(['387033866440962050','387037854846558209'])

# print(data2)

# tweet_dict = {}

# for idx in train_set_idx.keys():
#     for id in train_set_idx[idx]:
#         tweet_dict[id] = find_tweet_byID(id)


# print(tweet_dict)