import db.connectDB as conn
import db.handler.AccountsCommands as comands

class AccountsManagementt:
    """
    A class that represents my account management.It is used 
    for opperations in my data base that use data for accountusers
    tables and persondata.
    
    ...

    Atributes
    ---------
    connection : object
        An object that represents my connection with the data base
    cursor : object
        An object that executes my commands and commits changes in my database
    
    Methods
    -------
    def verifyLogIn(username, password)):
        This function has the role to verify is in account table 
        for login a user.
    def CreateAccount(username,password,firstName,lastName):
        This function is used for creating a user account with 
        data taken from parameeters if username isn't exists in
        database.
    """    
    def __init__(self):
        """
        Constructs all the necessary attributes for executing 
        comads for creating account operation or login operations

        Parameters
        ----------
        """
        self.connection = conn.connectDB()
        self.cursor = self.connection.cursor()
    
    def verifyLogIn(self, username, password):
        """
        This function has the role to verify is in account table 
        exists a user with pair (username,password) with help
        of cursor for executing comnads from AccountsCommands.py .
        If it exists it returns true,else it return False.If we have
        an error it will show the error.
        Parameters
        ----------
        username : str
            Is used for verify the username of the pretended user
        password : str
            Is used for verify the password of the pretended user
        """

        try:
            self.cursor.execute(comands.loginUser, (username, password))
            verifyLogIn = self.cursor.fetchone() is not None
            if verifyLogIn:
                return True
            else:
                return False
        except Exception as error_execComand:
            print(f"Error executing command login verify: {error_execComand}")
        finally:
            conn.endOperations(self.cursor, self.connection)
    
    def CreateAccount(self,username,password,firstName,lastName):
        """
        This function has the role to verify is in account table 
        exists a user with that username and if doesn't we can 
        create the new user and insert his personal data.Else
        it will return an error.
        Parameters
        ----------
        username : str
            Is used for inserting the username of the new user 
            if it doesn't already exists
        password : str
            Is used for inserting the password of the new user 
            if it doesn't already exists
        firstName : str
            Is used for inserting the firstName of the new user 
            if it doesn't already exists        
        lastName : str   
            Is used for inserting the lastName of the new user 
            if it doesn't already exists         
        """

        try:
            self.cursor.execute(comands.existsUsers,(username,))    
            if self.cursor.fetchone():
                print('The user Exists')
                return False
            else:
                self.cursor.execute(comands.createUser,(username,password))
                result = self.cursor.fetchone()
                if result is not None:
                    userid = result[0]
                    print("UserID generat:", userid)
                else:
                    print("Nu s-a generat niciun UserID")
                if userid is not None:    
                    print(userid)
                    self.cursor.execute(comands.addPerson,(userid,username,firstName,lastName))
                    self.connection.commit()
                    self.cursor.execute(comands.existsUsers, (username,))
                    if self.cursor.fetchone():
                        print("Inserare realizată cu succes.")
                        return True
                    else:
                        print("Inserarea nu a avut loc.")
                        return False
                else:
                    return False    
        except Exception as error_execComand:
            print(f"Error executing command creeate Account verify: {error_execComand}")
            
        finally:
            conn.endOperations(self.cursor, self.connection)
        