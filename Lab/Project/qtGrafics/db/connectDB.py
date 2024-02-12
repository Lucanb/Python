import psycopg2

def connectDB():
    """
    This function has the role to made a connection 
    with my data base and it is used in  different 
    classes and functions to execute different SQL
    comands.

    Parameters
    ----------
    """
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
    """
    This function has the role to close my cursor
    and my connection with the database after executing
    differents SQL comands in other classes or functions.

    Parameters
    ----------
    """

    print('End Operation')
    cursor.close()
    connection.close()