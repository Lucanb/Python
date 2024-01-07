import connectDB as conn
import create_tabels.tabelComands as commands

class MyTabels:
    def __init__(self):
        self.connection = conn.connectDB()
        self.cursor = self.connection.cursor()

    def creeateTabels(self):
        try:
            for command in commands.createTabelComands:
                self.cursor.execute(command)
                print("Succes, table created")

            self.connection.commit()
        except Exception as error_creatingTabels:
            print(f"Error at creating tabels: {error_creatingTabels}")
        finally:
            conn.endOperations(self.cursor, self.connection)