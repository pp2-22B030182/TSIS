# CREATE OR REPLACE PROCEDURE public.insert_list(
# 	IN p_id int,
# 	IN p_name character varying,
# 	IN p_phone_number character varying)
# LANGUAGE 'plpgsql'
# AS $BODY$
# begin
# 	insert into phonebook(id, name, number) values(p_id, p_name, p_phone_number);
# end;
# $BODY$;

data = [(55, 'Adikozha', '87023255484'), (66, 'olya', '87789777777'), (77, 'sake', '87778126349')]

import psycopg2

def insert_list(object):
    connection = None
    try:
        connection = psycopg2.connect(user="postgres",
                                    # пароль, который указали при установке PostgreSQL
                                    password="qwertyuiop",
                                    host="localhost",
                                    port="5432",
                                    database="pp2")

        # Создайте курсор для выполнения операций с базой данных
        cur = connection.cursor()
        cur.executemany('call insert_list(%s, %s, %s)', object)
        connection.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if connection is not None:
            connection.close()
            
insert_list(data)