from extract import extract_tweet 
from config import USER_NAME

tweet = extract_tweet()

def tweet_info()  : 

    data = tweet[USER_NAME]['TWEET_INFO']

    column_names = ["text", "favorite_count"  ,"date_creation" , "retweet_count" ]
    table_name = 'TWEET_INFO'
    table_data = [] 

    for  col1, col2, col3, col4 in zip (data['text'], data['favorite_count'] , data['created_at'] , data['retweet_count'] ) : 

        table_data.append((col1,col2,col3,col4))         

    return table_name, column_names , table_data

def user_info()  : 

    data = tweet[USER_NAME]['USER_INFO']

    column_names = ["followers", "following"  ,"date_creation" , "description" ]
    table_name = 'USER_INFO'
    table_data = [] 


    table_data.append((data['followers_count'] ,data['following_count'] , data['created_at']  , data['description']) )  

    return table_name, column_names , table_data

def activity_info()  : 
    
    data = tweet[USER_NAME]['USER_ACTIVITY']

    column_names = ["favorite_count", "retweet_count" ]
    table_name = 'USER_ACTIVITY'
    table_data = [] 
                               
    table_data.append( (data['favoris_count'] ,data['retweet_count'] ))         

    return table_name, column_names , table_data