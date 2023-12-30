import psycopg2
from psycopg2 import sql

def create_accounts_table(cursor):
    create_table_accounts = """
    CREATE TABLE accounts (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) UNIQUE,
        password VARCHAR(255)
    )
    """
    cursor.execute(create_table_accounts)

def create_persons_table(cursor):
    create_table_persons = """
    CREATE TABLE persons (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) UNIQUE,
        nume VARCHAR(255),
        prenume VARCHAR(255),
        FOREIGN KEY (username) REFERENCES accounts (username)
    )
    """
    cursor.execute(create_table_persons)


def create_meeting_table(cursor):
    create_table_meeting = """
    CREATE TABLE meeting (
        id SERIAL PRIMARY KEY,
        interval_orar TIMESTAMP,
        creator_id INTEGER,
        FOREIGN KEY (creator_id) REFERENCES persons (id)
    )
    """
    cursor.execute(create_table_meeting)

def create_invitations_table(cursor):
    create_table_invitations = """
    CREATE TABLE invitations (
        meeting_id INTEGER,
        person_id INTEGER,
        status VARCHAR(255) DEFAULT 'pending',
        FOREIGN KEY (meeting_id) REFERENCES meeting (id),
        FOREIGN KEY (person_id) REFERENCES persons (id)
    )
    """
    cursor.execute(create_table_invitations)

def creeateTabels():
    try:
        connection = psycopg2.connect(
            database = "meetingscheduler",
            user = "postgres",
            password='UFDHGEQS0727156236321', 
            host='127.0.0.1', 
            port= '5432'
        )

        cursor = connection.cursor()

        create_accounts_table(cursor)
        connection.commit()

        create_persons_table(cursor)
        connection.commit()

        create_meeting_table(cursor)
        connection.commit()

        create_invitations_table(cursor)
        connection.commit()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    creeateTabels()        