
import sys
sys.path.append('.')

import psycopg2
import csv
from extract_transform.utils import connection_object
import os
import datetime

def load_data_to_csv():

    date = str(datetime.datetime.now().date())
    conn = connection_object()
    cur = conn.cursor()

    for table in ['TWEET_INFO', 'USER_INFO', 'USER_ACTIVITY']:

        #retrieve data from database
        cur.execute(f"SELECT * FROM {table}")

        # retrieve the names of the columns
        headers = [desc[0] for desc in cur.description]

        # create a folder to store the data
        if not os.path.exists(r'./data'):
            os.makedirs(r'./data')

        # Use the csv library to write the data to a csv file
        with open(f'data/{table}_{date}.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(cur)

        # close the communication with the PostgreSQL
    conn.close()

if __name__ == '__main__':
    load_data_to_csv()