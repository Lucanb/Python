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
