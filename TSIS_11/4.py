# CREATE OR REPLACE FUNCTION public.getrows(
#   pagenumber integer,
#   pagesize integer)
#     RETURNS SETOF phonebook 
#     LANGUAGE 'plpgsql'
#     COST 100
#     VOLATILE PARALLEL UNSAFE
#     ROWS 1000

# AS $BODY$
#  BEGIN
#   RETURN QUERY
#    SELECT *
#    FROM phonebook
#    ORDER BY id
#    LIMIT PageSize
#    OFFSET PageNumber;
# END;
# $BODY$;

import psycopg2

def getrows(pagenumber, pagesize):
    conn = None
    try:
        conn = psycopg2.connect(user="postgres",
                                    # пароль, который указали при установке PostgreSQL
                                    password="qwertyuiop",
                                    host="localhost",
                                    port="5432",
                                    database="pp2")
        cur = conn.cursor()
        cur.execute('select * from getrows(%s, %s)', (pagenumber, pagesize))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

getrows(1, 2)