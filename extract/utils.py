import psycopg2
from config import DB_DETAILS

def postgres_connection(db_host, db_name, db_user, db_pass):
    
    connection = psycopg2.connect(f"dbname={db_name} user={db_user} host={db_host} password={db_pass}")

    return connection 

def connection_object(): 

    """ creates the object connection that connects us to the database """

    conn = postgres_connection(db_host = DB_DETAILS['db_host'],
                                db_name = DB_DETAILS['db_name'],
                                db_user = DB_DETAILS['db_user'],
                                db_pass = DB_DETAILS['db_pass'] ) 
    return conn