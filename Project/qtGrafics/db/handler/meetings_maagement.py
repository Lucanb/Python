import psycopg2
import db.handler.meetingsComands as comands
import db.connectDB as conn
from datetime import datetime

class MeetingManagement:
    def __init__(self):
        self.connection = conn.connectDB()     
        self.cursor = self.connection.cursor()  

    def selectMeetsById(self, idMeet):
        self.cursor.execute(comands.selectIdMeet, (idMeet,))
        return self.cursor.fetchall()

    def selectMeetsByTime(self,  ora_begin, ora_end):
        self.cursor.execute(comands.selectAllMeets, (ora_begin, ora_end))
        return self.cursor.fetchall()

    def createMeet(self,  creator_id, ora_begin, ora_end):
        self.cursor.execute(comands.addMeet, (creator_id, ora_begin, ora_end))
        return self.cursor.fetchone()[0]

    def deleteMeetAndInvitations(self,  meeting_id):
        self.cursor.execute(comands.deleteInviteID, (meeting_id,))
        self.cursor.execute(comands.deleteMeetID, (meeting_id,))

    def deleteInvitation(self,  meeting_id, person_id):
        self.cursor.execute(comands.deleteInviteMeetIDpersonID, (meeting_id, person_id))

    def getInvitationsByName(self,  person_name):
        self.cursor.execute(comands.allPersonInvites, (person_name, person_name))
        return self.cursor.fetchall()

    def getInvitationsByTime(self,  specific_time):
        self.cursor.execute(comands.allMeetInvites, (specific_time, specific_time))
        return self.cursor.fetchall()
