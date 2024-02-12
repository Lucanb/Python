import connectDB as conn
import create_tabels.tabelComands as commands

class MyTabels:
    """
    A class that represents my tabels,here we 
    create different tabels using a connection 
    function with my database
    
    ...

    Atributes
    ---------
    connection : object
        An object that represents my connection with the data base
    cursor : object
        An object that executes my commands and commits changes in my database

    Methods
    -------
    def creeateTabels():
       This is a function that has the role to use my cursor for executing
       creating tables command.It will return succes if my tabels are created
       or an error if they cannot be created.
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for executing 
        creating tabels operations.The atributes are connection
        and a cursor.

        Parameters
        ----------
        """

        self.connection = conn.connectDB()
        self.cursor = self.connection.cursor()

    def creeateTabels(self):
        """
        This function has the role to execute creating tabels
        command for my data base.And we use comand from tabelComands.py .

        Parameters
        ----------
        """
        
        try:
            for command in commands.createTabelComands:
                self.cursor.execute(command)
                print("Succes, table created")

            self.connection.commit()
        except Exception as error_creatingTabels:
            print(f"Error at creating tabels: {error_creatingTabels}")
        finally:
            conn.endOperations(self.cursor, self.connection)