import psycopg2
import db.connectDB as conn
import db.handler.personsComands as commands
import random

class PersonManagement:
    def __init__(self):
        self.connection = conn.connectDB()     
        self.cursor = self.connection.cursor()    
   
    def deleteUser(self, UserId):

        self.cursor.execute(commands.deleteInvPersonId, (UserId,))
        self.cursor.execute(commands.deleteMeetPersonId, (UserId,))
        self.cursor.execute(commands.deleteUserData, (UserId,))
        self.cursor.execute(commands.deleteAccount, (UserId,))
        # conn.endOperations(self.cursor,self.connection)

    def addUser(self, username, password, firstName, lastName):
        try:
            self.cursor.execute(commands.insertAccounts, (username, password))
            account_id = self.cursor.fetchone()[0]
            self.cursor.execute(commands.insertUserData, (account_id, username, firstName, lastName))
            self.connection.commit()
            print("Utilizatorul a fost adăugat cu succes.")
        except Exception as error_execComand:
            print(f"Eroare la executarea comenzii pentru adăugarea utilizatorului: {error_execComand}")
    
    def updateUserDataName(self,UserId, firstName, lastName):
        self.cursor.execute(commands.UpdateUserData, (firstName, lastName, UserId))

    def getUserAfterName(self, name):
        self.cursor.execute(commands.allPersonsAfterData, (name, name))
        return self.cursor.fetchall()
    
    def getUserId(self, username):
        self.cursor.execute(commands.getPersonId, (username,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    
    def searchPerson(self,firstName,lastName):
        self.cursor.execute(commands.searchPerson, (firstName, lastName))
        return self.cursor.fetchall()
    