import triggers_init.triggersComands as commands
import connectDB as conn


class myTriggers:
    """
    A class that creates my triggers for avoiding 
    programming errors.
    
    ...

    Atributes
    ---------
    connection : object
        An object that represents my connection with the data base
    cursor : object
        An object that executes my commands and commits changes in my database
    
    Methods
    -------
    def create_my_Triggers():
        This function has the role to create my triggers 
        for avoiding error programming.
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

    def create_my_Triggers(self):
        """
        This function has the role to create triggers for 
        avoiding eror programming.Firstly we will use 
        trigger creating comands from triggersComands.py 
        and when with our cursor we will execute them,commit 
        them and print Succes if trigger is created or error.
        """

        try:
            for command in commands.trigger_commands:
                self.cursor.execute(command)
                print("Succes, trigger created")

            self.connection.commit()

        except Exception as error_trigger:
            print(f"Error: {error_trigger}")

        finally:
            conn.endOperations(self.cursor,self.connection)


