# CREATE OR REPLACE FUNCTION public.pattern(
#   )
#     RETURNS TABLE(user_id integer, user_name character varying) 
#     LANGUAGE 'plpgsql'

# AS $$
# begin
#     return query
#     select snake_score.user_id, snake_score.user_name from snake_score where snake_score.user_name like '%ks%';
# end;
# $$;

# ALTER FUNCTION public.pattern()
#     OWNER TO postgres;
	
# select pattern()
import psycopg2
from psycopg2 import Error

connection = None

try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="qwertyuiop",
                                  host="localhost",
                                  port="5432",
                                  database="pp2")

    # Создайте курсор для выполнения операций с базой данных
    cursor = connection.cursor()

    cursor.callproc('pattern', ())

    row = cursor.fetchone()

    while row is not None:
        print(*row)
        row  = cursor.fetchone()

    connection.commit()
    print("Таблица успешно создана в PostgreSQL")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")