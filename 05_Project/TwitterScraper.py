import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import tweepy
import re
import config
from langdetect import detect_langs

def cleanTweet(tweet):
    clean_tweet = re.sub("@[A-Za-z0-9_]+", '', tweet)
    clean_tweet = re.sub("@[A-Za-z0-9_]+", '', clean_tweet)
    clean_tweet = re.sub("#[A-Za-z0-9_]+","", clean_tweet)
    clean_tweet = re.sub("https[://\/-zA-Z0-9_=+.$@#$%^&*()]+", '', clean_tweet)
    clean_tweet = re.sub("[^\w\s]", '', clean_tweet)
    clean_tweet = clean_tweet.lower()
    return clean_tweet

def fetchTweets(corpus_file_path, #Corpus file should have three columns: ID, Tweet, Location
                bearer_token,
                access_token, 
                access_token_secret,
                tweet_query, 
                max_results):

    #Import the existing corpus and IDs
    corpus = pd.read_csv(corpus_file_path)
    try:
        existing_ids = corpus['ID'].tolist()
    except:
        existing_ids = []
    
    #Authentication for Tweet Scraper
    client = tweepy.Client(bearer_token=bearer_token,
                            access_token=access_token,
                            access_token_secret= access_token_secret)

    if 'place_country' in tweet_query:
    #Fetches the Data given the query
        tweets = client.search_all_tweets(query=tweet_query, max_results=max_results, expansions =['geo.place_id'])
        places = {p['id']: p for p in tweets.includes['places']}
        has_location = True
    else:
        tweets = client.search_all_tweets(query=tweet_query, max_results=max_results)
        has_location = False


    #Sets up the table to organize the data
    names = ["ID", "Tweet", "Location"]
    tweet_df = pd.DataFrame(columns=names)
    tweet_dict = {}
    added = 0
    duplicates = 0

    for tweet in tweets[0]:
        print(tweet.created_at)
        tweet.id = str(tweet.id) + '-'
        if has_location == True and tweet.id not in existing_ids:
                place = places[tweet.geo['place_id']]
                clean_tweet = cleanTweet(tweet.text)
                tweet_dict["ID"] = tweet.id
                tweet_dict['Tweet'] = clean_tweet
                tweet_dict['Location'] = place
                tweet_df = tweet_df.append(tweet_dict, ignore_index=True)
                print("---------------")
                print("ID: %s" % tweet.id)
                print("Tweet: %s" % clean_tweet)
                print("Location: %s" % place)
                added += 1    
        elif tweet.id not in existing_ids and has_location == False:
                clean_tweet = cleanTweet(tweet.text)
                tweet_dict["ID"] = tweet.id
                tweet_dict['Tweet'] = clean_tweet
                tweet_dict['Location'] = 'None'
                tweet_df = tweet_df.append(tweet_dict, ignore_index=True)
                added += 1 
        else:
            duplicates +=1

    print("Duplicates:", duplicates)
    print("Added:", added)
    tweet_df.to_csv(corpus_file_path, encoding='utf-8-sig', float_format='{:f}'.format, mode='a', header=False, index=False)


fetchTweets(corpus_file_path="C:\\Users\\Jerem\\Desktop\\Fall2022\\L545\\ItalianData.csv", #Corpus file should have three columns: ID, Tweet, Location
                bearer_token=config.ACADEMIC_bearer_token,
                access_token=config.ACADEMIC_access_token, 
                access_token_secret=config.ACADEMIC_access_token_secret,
                tweet_query='morire -is:retweet', 
                max_results= 100)