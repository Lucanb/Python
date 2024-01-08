import db.connectDB as conn
import db.handler.AccountsCommands as comands

class AccountsManagementt:
    def __init__(self):
        self.connection = conn.connectDB()
        self.cursor = self.connection.cursor()
    
    def verifyLogIn(self, username, password):
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
        