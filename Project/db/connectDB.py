import psycopg2

def connectDB():

    print('Connecting...')
    
    try:
        connection = psycopg2.connect(
            database = "meetingscheduler",
            user = "postgres",
            password = 'UFDHGEQS0727156236321',
            host = '127.0.1',
            port = '5432'
        )
    
    except Exception as error_dbConnect:
        print(f"Connection error: {error_dbConnect}")

    print('Connection done!')

    return connection

def endOperations(cursor,connection):
    print('End Operation')
    cursor.close()
    connection.close()    