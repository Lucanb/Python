import psycopg2

connection = psycopg2.connect(
    database = "meetingscheduler",
    user = "postgres",
    password='UFDHGEQS0727156236321', 
    host='127.0.0.1', 
    port= '5432'
)

cursor = connection.cursor()

creeate_db = "CREATE DATABASE meetingscheduler;"
cursor.execute(creeate_db)

cursor.close()
connection.commit()

connection.close()