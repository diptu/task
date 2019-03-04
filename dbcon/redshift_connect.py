#!/usr/bin/python
import psycopg2
from config import config


# Simple routine to run a query on a database and print the results:
def create_table( conn ) :
    cur = conn.cursor()
    cur.execute("""\

    CREATE TABLE IF NOT EXISTS FACT(

        membership_no character varying(255),
        first_free_join_date character varying(255),
        last_free_subscription_date character varying(255),
        first_piad_subscription_date character varying(255),
        last_piad_subscription_date character varying(255),
        number_of_renew_performed character varying(255),
        number_of_paid_subscription character varying(255),
        first_retailer_or_channel character varying(255),
        avg_membership_duration character varying(255)

        );

     """)
    conn.commit()


# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()
    cur.execute("""\
    SELECT *
     FROM FACT
     limit 10
     """)

    print("The number of parts : ", cur.rowcount)
    row = cur.fetchone()

    while row is not None:
        print(row)
        row = cur.fetchone()
def redshift_connect():
    """ Connect to the redshift database server """
    conn = None
    try:
        # read connection parameters
        params = config('redshift.ini')

        # connect to the redshift server
        print('Connecting to the redshift database...')
        conn = psycopg2.connect(**params)
        create_table( conn )
        doQuery( conn )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            
if __name__ == '__main__':
    redshift_connect()
