import requests
import tweepy
import json

"""This file only focuses on english tweets and does not saves small sized, empty or private users"""


tweet_fields = [
    "author_id",
    "created_at",
    "edit_controls",
    "edit_history_tweet_ids",
    "geo",
    "id",
    "in_reply_to_user_id",
    "lang",
    "referenced_tweets",
    "reply_settings",
    "source",
    "text"]
tweet_fields = [x.strip(' ') for x in tweet_fields]
expansions = [

    "author_id",
    "edit_history_tweet_ids",
    "entities.mentions.username",
    "geo.place_id",
    "in_reply_to_user_id",
    "referenced_tweets.id",
    "referenced_tweets.id.author_id"]
expansions = [x.strip(' ') for x in expansions]
user_fields = [
    "created_at",
    "id",
    "location",
    "name"]
user_fields = [x.strip(' ') for x in user_fields]
place_fields = [
    "contained_within",
    "country",
    "country_code",
    "full_name",
    "geo",
    "id",
    "name",
    "place_type"]
place_fields = [x.strip(' ') for x in place_fields]

# key changed
client = tweepy.Client(
    "AAAAAAAAAAAAAAAAAAAAAI7bhAEAAAAAXFbXlYNurx1fRppFCVVGXDvzN%2Fg%3DNhhRAsbFWklw6dD2LVzhKJuCMmVzsn37l4t7JmlJN07UpEYjAw",
    return_type=requests.Response, wait_on_rate_limit=True)


def parse(d):
    authors = []
    # Removes curly braces and splits the pairs into a list
    linee = d.strip('{}').split(', ')
    for i in linee:
        authors.append(i.strip("'"))
    return authors


def dumper(user_no):
    tweet_data = {"data": {user_no: []}}
    try:
        for tweet in tweepy.Paginator(client.get_users_tweets, id=user_no,
                                      max_results=100,
                                      end_time="2022-10-26T00:00:01Z",
                                      exclude="retweets",
                                      expansions=expansions,
                                      place_fields=place_fields,
                                      tweet_fields=tweet_fields,
                                      user_fields=user_fields):
            tweet_data["data"][user_no].append(tweet.json())
    except AttributeError:
        pass

    return json.dumps(tweet_data, indent=4)


filename = '../Other Data/author-ids-to-be-extracted-4.txt'
with open(filename, 'r') as file:
    lines = file.read().splitlines()
    author_list = []
    for line in lines:
        author_list.append(parse(line))
    flat_list = [item for sublist in author_list for item in sublist]
    print(len(flat_list))
    for author in flat_list[5000:]:
        with open(f'{author[1:-1]}.json', 'w') as f:
            f.write(dumper(author))
