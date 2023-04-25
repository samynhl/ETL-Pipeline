from utils import connection_object
from extract_transform import extract_tweet 
from config import USER_NAME
from table import user_info, tweet_info, activity_info

def query(table_name, column_names):
    
    col_name = ', '.join(column_names)
    col_val = tuple(map(lambda column: column.replace(column, '%s'), column_names))
    column_val_string = ', '.join(col_val)
    query_text = (f'''
        INSERT INTO {table_name} ({col_name}) VALUES ({column_val_string})
    ''')

    return query_text

def insert(conn, query, cursor, table_data, batch=20):

    records = [] 
    count = 1 

    for raw in table_data:

        records.append(raw)

        if count % batch == 0:
            cursor.executemany(query, records)
            conn.commit()
            records = []

        count = count + 1


    cursor.executemany(query, records)
    conn.commit()


def write(table_name, column_names, table_data) : 

    conn = connection_object()
    cursor = conn.cursor()

    query_insert = query(table_name, column_names)

    insert(conn,query_insert,  cursor, table_data)

    conn.close()
    cursor.close()

if __name__ == '__main__' : 

    write(tweet_info()[0], tweet_info()[1],tweet_info()[2] )
    write(user_info()[0], user_info()[1],user_info()[2] )
    write(activity_info()[0], activity_info()[1],activity_info()[2] )