import tweepy
from  config import USER_KEY, USER_NAME

def extract_tweet(user_name = USER_NAME)  : 

    """ allows you to retrieve all the data related to the user account and to store the data as a dictionary """

    access_key = USER_KEY['access_key']
    access_secret = USER_KEY['access_secret'] 
    consumer_key = USER_KEY['consumer_key']
    consumer_secret = USER_KEY['consumer_secret']

    print(access_key)
    print(access_secret)
    print(consumer_key)
    print(consumer_secret)

    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)   
    auth.set_access_token(consumer_key, consumer_secret) 

    # Creating an API object 
    api = tweepy.API(auth)

    # store info 

    infos = {
        user_name: {
            "TWEET_INFO": {
                "text": [] ,
                "favorite_count":[] ,
                "retweet_count": [],
                "created_at":[]
            },
            "USER_INFO": {
                "followers_count": '' ,
                "following_count": '',
                "created_at":'' ,
                "description":'' ,
            },
            "USER_ACTIVITY": {
                "favoris_count":'' ,
                "retweet_count":'' ,
            }
        }
    }

    # get user tweets 
    tweets = api.user_timeline(screen_name='@'+str(user_name), 
                            count=50,
                            include_rts = False,
                            tweet_mode = 'extended') 

    # retrieves tweets
    for tweet in tweets : 
        infos[user_name]["TWEET_INFO"]['text'].append(tweet._json["full_text"])
        infos[user_name]["TWEET_INFO"]['favorite_count'].append(tweet.favorite_count)
        infos[user_name]["TWEET_INFO"]['retweet_count'].append(tweet.retweet_count)
        infos[user_name]["TWEET_INFO"]['created_at'].append(tweet.created_at)
  
    # Retrieving account information
    user = api.get_user( screen_name = user_name)
    
    infos[user_name]["USER_INFO"]['followers_count'] =  user.followers_count
    infos[user_name]["USER_INFO"]['following_count'] = user.friends_count
    infos[user_name]["USER_INFO"]['created_at'] = user.created_at
    infos[user_name]["USER_INFO"]['description'] = user.description

    infos[user_name]["USER_ACTIVITY"]['favoris_count'] =  user.favourites_count
    infos[user_name]["USER_ACTIVITY"]['retweet_count'] =  user.statuses_count
    
    return infos     


if __name__ == '__main__' :

    print('extracting')
    extract_tweet() 
    print('extracting done')
