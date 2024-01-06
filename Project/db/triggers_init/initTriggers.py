import triggers_init.triggersComands as commands
import connectDB as conn


class myTriggers:
    def __init__(self):
        self.connection = conn.connectDB()
        self.cursor = self.connection.cursor()

    def create_my_Triggers(self):
        try:
            for command in commands.trigger_commands:
                self.cursor.execute(command)
                print("Succes, trigger created")

            self.connection.commit()

        except Exception as error_trigger:
            print(f"Error: {error_trigger}")

        finally:
            conn.endOperations(self.cursor,self.connection)


