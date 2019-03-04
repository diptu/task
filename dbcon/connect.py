#!/usr/bin/python
import psycopg2
from config import config
from redshift import redshift_connect


# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()
    cur.execute("""\


                SELECT

                  distinct m.membership_no,
                  a.FFJD as first_free_join_date,
                  a.LFJD as last_free_subscription_date,
                  b.FPJD as first_piad_subscription_date,
                  b.LPJD as last_piad_subscription_date,
                  c.renue as number_of_renew_performed,
                  d.no_paid_subs as number_of_paid_subscription,
                  e.retailer_type as first_retailer_or_channel,
                  f.membership_duration avg_membership_duration

                FROM
                	( SELECT distinct membership_no
                	 FROM public.subscription_data
                  	) m
                FULL OUTER JOIN

                  ( SELECT  membership_no, MIN(subscription_on) as FFJD, MAX(subscription_on) as LFJD
                	FROM public.subscription_data
                	WHERE current_product_code in('TonicBasic')
                    GROUP BY membership_no
                  	) a
                ON
                  m.membership_no =  a.membership_no

                FULL OUTER JOIN
                  ( SELECT membership_no, MIN(subscription_on) as FPJD , MAX(subscription_on) as LPJD
                	FROM public.subscription_data
                	WHERE current_product_code not in('TonicBasic')
                     GROUP BY membership_no
                  	) b
                ON
                 m.membership_no =  b.membership_no

                 FULL OUTER JOIN
                  ( SELECT membership_no , count(subscription_status) as renue
                	 FROM public.subscription_data
                	 where subscription_status='RENEW'
                	 group by membership_no
                  	) c
                ON
                 m.membership_no =  c.membership_no
                 FULL OUTER JOIN
                 ( SELECT membership_no, COUNT(subscription_status) as no_paid_subs
                	FROM public.subscription_data
                	WHERE subscription_status='UPGRADE' OR subscription_status='RENEW'
                  GROUP BY membership_no ) d
                 ON m.membership_no =  d.membership_no

                  FULL OUTER JOIN
                 	(SELECT membership_no,MIN(subscription_on), retailer_type
                	FROM public.subscription_data
                	WHERE retailer_type IS NOT NULL
                  	GROUP BY (membership_no,retailer_type)) e
                 ON m.membership_no =  e.membership_no

                	FULL OUTER JOIN
                 	(select  membership_no ,
                	 AVG(CURRENT_TIMESTAMP - TO_TIMESTAMP(subscription_on, 'DD-MM-YYYY HH24:MI:SS.US'))
                	as membership_duration
                	FROM public.subscription_data
                	group by membership_no) f
                 ON m.membership_no =  f.membership_no
                 ;


     """)

    print("The number of parts : ", cur.rowcount)

    # for row in cur.fetchall():
    #     print(row)
    fact_obj = cur.fetchall()
    redshift_connect(fact_obj)
    # for obj in fact_obj:
    #     print(obj)

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        doQuery( conn )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
