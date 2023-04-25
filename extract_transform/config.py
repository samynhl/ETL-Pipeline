from dotenv import load_dotenv
import os
load_dotenv(r'./extract_transform/.env')

USER_KEY = { 
        "access_key" : os.getenv("ACCESS_KEY")  ,
        "access_secret" : os.getenv("ACCESS_SECRET"),
        "consumer_key" : os.getenv("CONSUMER_KEY"),
        "consumer_secret" : os.getenv("CONSUMER_SECRET")
} 


DB_DETAILS = {
            'db_name': os.getenv("DB_NAME"),
            'db_user': os.getenv("DB_USER"),
            'db_host': 'postgresdb',
            'db_pass': os.getenv("DB_PASS")
} 


USER_NAME = 'elonmusk'