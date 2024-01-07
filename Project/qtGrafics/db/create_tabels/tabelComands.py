
create_table_accounts = """
        CREATE TABLE accountUsers (
            userId SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE,
            password VARCHAR(255)
        )
        """
create_table_persons = """
        CREATE TABLE personData (
            personId INTEGER UNIQUE, 
            nume VARCHAR(255),
            prenume VARCHAR(255),
            FOREIGN KEY (personId) REFERENCES accountUsers(userId)
        )
        """
create_table_meeting = """
        CREATE TABLE meetingAppointments (
            meetingId SERIAL PRIMARY KEY,
            hour_begin TIMESTAMP,
            hour_end TIMESTAMP,
            hostId INTEGER,
            FOREIGN KEY (hostId) REFERENCES personData (personId)
        )
        """
create_table_invitations = """
        CREATE TABLE invitations (
            meetingId INTEGER,
            personId INTEGER,
            status VARCHAR(255) DEFAULT 'waiting',
            FOREIGN KEY (personId) REFERENCES personData (personId),
            FOREIGN KEY (meetingId) REFERENCES meetingAppointments (meetingId)
        )
        """

createTabelComands = [create_table_accounts,create_table_persons,
                      create_table_meeting,create_table_invitations]
