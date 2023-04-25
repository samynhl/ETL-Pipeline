from utils import connection_object

def create_tables() : 

    conn = connection_object()
    cursor = conn.cursor()

    # create user info
    cursor.execute('''CREATE TABLE IF NOT EXISTS USER_INFO (followers INT, following INT, date_creation DATE, description VARCHAR)''')

    # create tweet info 
    cursor.execute('''CREATE TABLE IF NOT EXISTS TWEET_INFO (text VARCHAR, favorite_count INT, date_creation DATE, retweet_count INT)''')

    # create user activity 
    cursor.execute('''CREATE TABLE IF NOT EXISTS USER_ACTIVITY (favorite_count INT,retweet_count INT)''')

    conn.commit()
    cursor.close()
    conn.close()



if __name__ =='__main__' : 
    create_tables()