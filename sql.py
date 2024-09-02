import psycopg2

from config import host,user,password,db_name,monkes

def insert_user(connection, nickname, chatid):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO users (nickname,chatid) VALUES
            ('{nickname}',{chatid})"""
        )

def insert_photo(connection,url):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO photo_monkey (url) VALUES
            ('{url}')"""
        )

def delete_user(connection,chatid):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""DELETE FROM users WHERE chatid = {chatid};"""
        )
    

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True 

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE photo_monkey(
    #         id serial PRIMARY KEY,
    #         url varchar)
    #         """
    #     )
    # connection.commit()
    for i in monkes:
        insert_photo(connection,url=i)
    
    
except Exception as _ex:
    print(f"Не удалось подключиться к бд: {_ex}")
finally:
    if connection:
        connection.close()
        print("Бдшка закрыта")