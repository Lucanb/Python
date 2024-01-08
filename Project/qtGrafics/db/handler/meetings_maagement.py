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

    def createMeet(self, creator_id, ora_begin, ora_end):
        try:
            self.cursor.execute(comands.addMeet, (creator_id, ora_begin, ora_end))
            meetId = self.cursor.fetchone()[0]
            self.connection.commit()
            return meetId
        except Exception as e:
            print("Error creating meet:", str(e))
            self.connection.rollback()
            return None

    def deleteMeetAndInvitations(self, meeting_id):
        try:
            self.cursor.execute(comands.deleteInviteID, (meeting_id,))
            self.cursor.execute(comands.deleteMeetID, (meeting_id,))
            self.connection.commit()
        except Exception as e:
            print("Error deleting meeting and invitations:", str(e))
            self.connection.rollback()

    def deleteInvitation(self, meeting_id, person_id):
        try:
            self.cursor.execute(comands.deleteInviteMeetIDpersonID, (meeting_id, person_id))
            self.connection.commit()
        except Exception as e:
            print("Error deleting invitation:", str(e))
            self.connection.rollback()

    def getInvitationsByName(self, person_name):
        self.cursor.execute(comands.allPersonInvites, (person_name, person_name))
        return self.cursor.fetchall()

    def getInvitationsByTime(self, specific_time):
        self.cursor.execute(comands.allMeetInvites, (specific_time, specific_time))
        return self.cursor.fetchall()

    def getMeetsInvitationsById(self, id):
        self.cursor.execute(comands.allMeetInvById, (id, id))
        return self.cursor.fetchall()
    
    def getInvitationByIdUserAndIdMeet(self,idUser,idMeet):
            self.cursor.execute(comands.InvitationByNameAndIdMeet, (idUser, idMeet))
            return self.cursor.fetchall()

        
    def addInvitation(self, meetingId, personId):
        try:
            self.cursor.execute(comands.addInvite, (meetingId, personId))
            self.connection.commit()
        except Exception as e:
            print("Error adding invitation:", str(e))
            self.connection.rollback()
    
    def getMeetAfterId(self,meetingId):
            self.cursor.execute(comands.getMeetAfterId, (meetingId,))
            return self.cursor.fetchall()        