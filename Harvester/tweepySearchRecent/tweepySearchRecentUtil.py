import random

import tweepy
from datetime import datetime
from time import sleep


### Task1 get all tweetAPI
def getClient(tweetAPI):
    return tweepy.Client(bearer_token=tweetAPI['bearer_token'],
                         consumer_key=tweetAPI['consumer_key'],
                         consumer_secret=tweetAPI['consumer_secret'],
                         access_token=tweetAPI['access_token_key'],
                         access_token_secret=tweetAPI['access_token_secret'])


### Task2 retrieve couchdb
def retrieve_couchdb(servers, serverName):
    try:
        database = servers[serverName] if serverName in servers else servers.create(serverName)
    except Exception as e:
        database = servers.create("new_" + serverName)
    return database

### Task3 implement search tweepy
### User rate limit (OAuth 2.0 user Access Token): 180 requests per 15-minute
### add sleep function
def crawlTweets(clients, database):
    runningTime = 0

    while True:
        # detect duplicate case
        dupCount = 0
        allCount = 0
        startTime = datetime.now().second
        for c, client in enumerate(clients):
            # change query each time
            try:
                for i, tweets in enumerate(tweepy.Paginator(
                        client.search_recent_tweets,
                        query="#melbourne lang:en",
                        tweet_fields=[
                            'context_annotations',
                            'created_at',
                            'geo',
                            'lang',
                            'conversation_id',
                            'public_metrics',
                            'referenced_tweets',
                            'in_reply_to_user_id',
                        ],
                        user_fields=[
                            'profile_image_url',
                            'name',
                            'username',
                            'created_at',
                            'description',
                            'entities',
                            'location',
                            'protected',
                            'public_metrics',
                            'verified',
                        ],
                        media_fields=[
                            "media_key",
                            "type",
                            "duration_ms",
                            "public_metrics",
                            "width",
                            "height",
                            "preview_image_url",
                            "alt_text"
                        ],
                        expansions=[
                            "author_id",
                            "referenced_tweets.id",
                            "referenced_tweets.id.author_id",
                            "attachments.media_keys",
                        ],
                        max_results=100
                )):
                    startTimeSlot = datetime.now().second
                    users = {u["id"]: u for u in tweets.includes['users']}
                    media = {media["media_key"]: media for media in
                             tweets.includes.get("media")} if tweets.includes.get("media") else None
                    for j, tweet in enumerate(tweets.data):
                        user = users[tweet.author_id]

                        # get media
                        attachments = tweet['attachments']
                        media_keys = attachments.get('media_keys') if attachments else None
                        tweet_media = media.get(media_keys[0] if media_keys else media_keys) if media else None

                        tweet_crawl = {
                            "_id": str(tweet.id),
                            "tweet_text": tweet.text,
                            "tweet_created_at": tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                            "tweet_public_metrics": tweet.public_metrics,
                            "tweet_in_reply_to_user_id": tweet.in_reply_to_user_id,
                            "tweet_conversation_id": tweet.conversation_id,
                            "tweet_context_annotations": tweet.context_annotations,
                            "tweet_geo": tweet.geo,
                            "tweet_lang": tweet.lang,
                            "tweet_reference_id": str(
                                [objectR.id for objectR in tweet.referenced_tweets]) if tweet.referenced_tweets else None,
                            "tweet_reply_id": str(tweet.in_reply_to_user_id) if tweet.in_reply_to_user_id else None,

                            "author_id": user.id,
                            "author_created_at": user.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                            "author_location": user.location,
                            "author_public_metrics": user.public_metrics,

                            "media_type": tweet_media.get("media_type") if tweet_media else None,
                            "media_view_count": (
                                tweet_media.get("public_metrics").get("view_count")
                                if tweet_media and
                                   tweet_media.get("public_metrics") and
                                   tweet_media["public_metrics"].get("view_count")
                                else None
                            ),
                        }
                        allCount += 1
                        if str(tweet.id) not in database:
                            database.save(tweet_crawl)
                        else:
                            print("dup")
                            dupCount += 1
                    print("api: ", c, "progress: ", i + 1, '/', 180)
                    # don't too fast
                    endTimeSlot = datetime.now().second
                    if endTimeSlot - startTimeSlot < 2.5:
                        sleep(3 - (endTimeSlot - startTimeSlot))
                    if i == 90:
                        break
            except:
                break
        #stop when many duplicate exist
        if dupCount / allCount >= 0.98 and runningTime >= 5000:
            break
        runningTime += 1
        endTime = datetime.now().second
        if endTime - startTime < 3600:
            sleep(3600 - (endTime - startTime))
