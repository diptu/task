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
def doQuery( conn,fact_obj ) :
    cur = conn.cursor()

    for obj in fact_obj:
        membership_no, first_free_join_date, last_free_subscription_date, first_piad_subscription_date,last_piad_subscription_date,number_of_renew_performed,number_of_paid_subscription, first_retailer_or_channel,avg_membership_duration = obj
        cur.execute("INSERT INTO FACT VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" %  (membership_no, first_free_join_date, last_free_subscription_date, first_piad_subscription_date,last_piad_subscription_date,number_of_renew_performed,number_of_paid_subscription, first_retailer_or_channel,avg_membership_duration ))

    conn.commit()
    # for obj in fact_obj:
    #     print(fact_obj)


def redshift_connect(fact_obj=None):
    """ Connect to the redshift database server """
    conn = None
    try:
        # read connection parameters
        params = config('redshift.ini')

        # connect to the redshift server
        print('Connecting to the redshift database...')
        conn = psycopg2.connect(**params)
        create_table( conn )
        doQuery( conn,fact_obj )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
