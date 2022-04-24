import os
import logging

import tweepy
from tweepy import StreamingClient, StreamRule, Tweet

class TweetListener(StreamingClient):
    def on_tweet(self, tweet: Tweet):
        print(tweet.__repr__())
    def on_request_error(self, status_code):
        print(status_code)
    def on_connection_error(self):
        self.disconnect()

if __name__ == "__main__":
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAAjObQEAAAAATW9tC0iazrmCdQAiVn9ZAy4sne0%3DR87gTUcD1IhnzH52iAbGvBQMqTBNG1LeNraXmHMIAr8EuVee8o"

    client = TweetListener(bearer_token)

    rules = [ StreamRule(value="melbourne")]

    resp = client.get_rules()
    if resp and resp.data:
        rule_ids = []
        for rule in resp.data:
            rule_ids.append(rule.id)
        client.delete_rules(rule_ids)

    # validate the rule
    resp = client.add_rules(rules, dry_run = True)
    if resp.errors:
        raise RuntimeError

    # add the rule
    resp =client.add_rules(rules)
    if resp.errors:
        raise RuntimeError(resp.errors)
    print(client.get_rules())

    try:
        client.filter()
    except KeyboardInterrupt:
        client.disconnect()