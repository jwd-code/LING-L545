import pandas as pd
import tweepy
import re
import config
import warnings
import csv
warnings.simplefilter(action='ignore', category=FutureWarning)
from datetime import date


def update_log(log_file_path, query, added, duplicates):
    today = date.today()
    when = today.strftime("%b-%d-%Y")
    new_record = [query, added, duplicates, when]
    with open(log_file_path, 'a') as lf:
        writer = csv.writer(lf)
        writer.writerow(new_record)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!






def cleanTweet(tweet):
    clean_tweet = re.sub("@[A-Za-z0-9_]+", '', tweet)
    clean_tweet = re.sub("@[A-Za-z0-9_]+", '', clean_tweet)
    clean_tweet = re.sub("#[A-Za-z0-9_]+","", clean_tweet) 
    clean_tweet = re.sub("https[://\/-zA-Z0-9_=+.$@#$%^&*()]+", '', clean_tweet) #Get rid of links
    clean_tweet = re.sub("[^\w\s]", '', clean_tweet)
    clean_tweet = clean_tweet.lower()
    return clean_tweet

def fetchTweets(log_file_path,
                corpus_file_path, #Corpus file should have three columns: ID, Tweet, Location
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


    #Get the tweets
    tweets = client.search_all_tweets(query=tweet_query, max_results=max_results)
  

    #Sets up the table to organize the data
    names = ["ID", "Tweet"]
    tweet_df = pd.DataFrame(columns=names)
    tweet_dict = {}
    added = 0
    duplicates = 0

    #Get the tweets, clean them, print them, add them to a dictionary
    for tweet in tweets[0]:
        print(tweet.created_at)
        tweet.id = str(tweet.id) + '-'
        if tweet.id not in existing_ids:
                clean_tweet = cleanTweet(tweet.text)
                tweet_dict["ID"] = tweet.id
                tweet_dict['Tweet'] = clean_tweet
                tweet_df = tweet_df.append(tweet_dict, ignore_index=True)
                print("---------------")
                print("ID: %s" % tweet.id)
                print("Tweet: %s" % clean_tweet)
                added += 1    
        else:
            duplicates +=1

    print("Duplicates:", duplicates)
    print("Added:", added)
    tweet_df.to_csv(corpus_file_path, encoding='utf-8-sig', float_format='{:f}'.format, mode='a', header=False, index=False)
    update_log(log_file_path=log_file_path, query=tweet_query, added=added, duplicates=duplicates)


fetchTweets(log_file_path='C:\\Users\\Jerem\\Documents\\Fall 2022\\L-545\\Final Project\\Data\\log.csv',
            corpus_file_path="C:\\Users\\Jerem\\Documents\\Fall 2022\\L-545\\Final Project\\Data\\ItalianData.csv", #Corpus file should have two columns: ID, Tweet
            bearer_token=config.ACADEMIC_bearer_token,
            access_token=config.ACADEMIC_access_token, 
            access_token_secret=config.ACADEMIC_access_token_secret,
            tweet_query='"sono molto triste" -is:retweet', 
            max_results= 200)

