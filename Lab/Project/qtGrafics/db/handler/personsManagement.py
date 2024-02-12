import psycopg2
import db.connectDB as conn
import db.handler.personsComands as commands
import random

class PersonManagement:
    """
    A class that represents my person management.It is used 
    for opperations in my data base that use data for persondata
    
    ...

    Atributes
    ---------
    connection : object
        An object that represents my connection with the data base
    cursor : object
        An object that executes my commands and commits changes in my database
    
    Methods
    -------
    def deleteUser(userId):
        This function has the role to verify is in account table 
        for login a user.
    def addUser(username,password,firstName,lastName):
        This function is used for creating a user account with 
        data taken from parameeters if username isn't exists in
        database.
    def updateUserDataName(self,UserId, firstName, lastName):
        This function has the role to update first name and lastname 
        of a user after its id.
    def getUserAfterName(self, name):
        This function has the role to get a user after it's name.
    def getUserId(self, username):
        This function has the role to return an id of a user after it's name
    def searchPerson(self,firstName,lastName):
        This function has the role to show all persons after
        first name and last name.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for executing 
        different comads that manipulate user datas.The atributes are connection
        and a cursor.

        Parameters
        ----------
        """        
        self.connection = conn.connectDB()     
        self.cursor = self.connection.cursor()    
   
    def deleteUser(self, UserId):
        """
        This function has the role to verify is in account table 
        exists a user , then if it exists it will delete all its invites,
        then itis meeteings and the the useri itself,
        ----------
        UserId : Integer
            Is used for verify the user ID
        """
        self.cursor.execute(commands.deleteInvPersonId, (UserId,))
        self.cursor.execute(commands.deleteMeetPersonId, (UserId,))
        self.cursor.execute(commands.deleteUserData, (UserId,))
        self.cursor.execute(commands.deleteAccount, (UserId,))
        # conn.endOperations(self.cursor,self.connection)

    def addUser(self, username, password, firstName, lastName):
        """
        This function has the role to verify is in account table 
        exists a user , then if it exists then it will print an error
        that the user cannot be added,else it will say it was added with succes,
        ----------
        username : str
            Is used for verify the user username
        password : str
            It adds a user password
        firstName : str 
            It adds its firstname
        lastName : str 
            It adds its lastname    
        """
        try:
            self.cursor.execute(commands.insertAccounts, (username, password))
            account_id = self.cursor.fetchone()[0]
            self.cursor.execute(commands.insertUserData, (account_id, username, firstName, lastName))
            self.connection.commit()
            print("Utilizatorul a fost adăugat cu succes.")
        except Exception as error_execComand:
            print(f"Eroare la executarea comenzii pentru adăugarea utilizatorului: {error_execComand}")
    
    def updateUserDataName(self,UserId, firstName, lastName):
        """
        This function has the role to update user data
        ----------
        UserId : Integer
            Is used for verify the user username
        password : str
            It adds a user password
        firstName : str 
            It update its firstname
        lastName : str 
            It update its lastname    
        """
        self.cursor.execute(commands.UpdateUserData, (firstName, lastName, UserId))

    def getUserAfterName(self, name):
        """
        This function has the role to return all persons after name
        ----------
        name : str
            Is used search all persons names   
        """
        self.cursor.execute(commands.allPersonsAfterData, (name, name))
        return self.cursor.fetchall()
    
    def getUserId(self, username):
        """
        This function has the role to return all persons id's if exists 
        or None in other case
        ----------
        username : str
            Is used to get the person id  
        """
        self.cursor.execute(commands.getPersonId, (username,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    
    def searchPerson(self,firstName,lastName):
        """
        This function has the role to return all persons after first and name
        ----------
        firstName : str
            It is userd to search all persons after first name
        name : str
            Is used search all persons after last name   
        """
        self.cursor.execute(commands.searchPerson, (firstName, lastName))
        return self.cursor.fetchall()
    