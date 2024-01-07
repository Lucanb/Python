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
        conn.endOperations(self.cursor,self.connection)

    def addUser(self,username, password,firstName,lastName):
        self.cursor.execute(commands.insertAccounts, (username, password))
        account_id = self.cursor.fetchone()[0]
        self.cursor.execute(commands.insertUserData, (account_id, firstName, lastName))
        conn.endOperations(self.cursor,self.connection)
    
    def updateUserDataName(self,UserId, firstName, lastName):
        self.cursor.execute(commands.UpdateUserData, (firstName, lastName, UserId))

    def getUserAfterName(self, name):
        self.cursor.execute(commands.allPersonsAfterData, (name, name))
        conn.endOperations(self.cursor,self.connection)
        return self.cursor.fetchall()