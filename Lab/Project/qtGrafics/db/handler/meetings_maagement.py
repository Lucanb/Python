import psycopg2
import db.handler.meetingsComands as comands
import db.connectDB as conn
from datetime import datetime

class MeetingManagement:
    """
    A class that represents my meetings management.It is used 
    for opperations in my data base that use data for meetings
    
    ...

    Atributes
    ---------
    connection : object
        An object that represents my connection with the data base
    cursor : object
        An object that executes my commands and commits changes in my database
    
    Methods
    -------
    def selectMeetsById(idMeet):
        This function has the role to select a meeting after its id.
    def selectMeetsByUserId(username,password,firstName,lastName):
        This function has the role to select a meeting after its id.
    def selectMeetsByTime(ora_begin, ora_end):
        This function has the role to select all my meets after
        a time interval
    def createMeet(creator_id, ora_begin, ora_end):
        This function has the role to create a meet after my userId and
        hour interval.
    def deleteMeetAndInvitations(meeting_id):
        This function has the role to delete all invitations after
        meeting_id and then it deletes all meeting after this meeting_id 
        if it exists.
    def deleteInvitation(meeting_id, person_id):
        This function has the role to delete all invitations after meeting_id
        and personid.
    def getInvitationsByName(person_name):
        This function has the role to return an Invitation after a person name if that one exists.

    def getInvitationsByTime(specific_time):
        This function has the role to get my invitations at a specific time.

    def getMeetsInvitationsById(id):
        This function has the role to get our meets and invitations data after id.
    
    def getInvitationByIdUserAndIdMeet(idUser,idMeet):
        This function return all Meetings and invitations after 
        our introduce idUser and id Meet if those exists.
        
    def addInvitation(meetingId, personId):
        Tis function has the role to add in my database 
        an invitation if there exists meetingId and personId.
    
    def getMeetAfterId(meetingId):
        This function has the role to get a meet after it's meeting id.
    
    def getInvitations(username):
        This function has the role to get all invitations after username.

    def meetingExists(meeting_id, user_id):
        This function will verify if there exists a meeing with meeting_id 
        and host_id from parameeters.
    
    def invitationExists(self,meeting_id, user_id):
        This function will verify if there exists a invitation with meeting_id 
        and user_id from parameeters.     

    def createInvitation(self,meeting_id, user_id):
        This method has  the role to creeate an invitation if 
        it doesn't exists after meeting_id and user_id.It will returns
        True if it is possible and False if it is not.                 
        
    def createMeetImport(self,meet_id,creator_id, ora_begin, ora_end):
        This function returns meetId if we could create that 
        meet or None in other case.The meet is created with function 
        parameeters which represints data from import. 
    
    def invitationExistsMeetID(self,meetID):
        This function has the role to verify if there exists a meeting after that ID
    
    def deleteInvitationMeetID(self,meetID):
        This function has the role to delete an invitation 
        that has a meet id.
    
    def deleteMeetJustID(self,meetID):
        This function delete a meete with a specific meetID.
    
    def searchInvitaion(self,idUser):
        This function has the role to search an invitation after an idUser if that id exists.   
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for executing 
        different comads that manipulate meetings or invites datas.The atributes are connection
        and a cursor.

        Parameters
        ----------
        """   

        self.connection = conn.connectDB()     
        self.cursor = self.connection.cursor()  

    def selectMeetsById(self, idMeet):
        """
        This function has the role to get all meetings after an idMeet
        Parameters
        ----------
        idMeet : Integer
            It is used for searching a meet after an meeting id.        
        """    
        self.cursor.execute(comands.selectIdMeet, (idMeet,))
        return self.cursor.fetchall()
    
    def selectMeetsByUserId(self, hostId):
        """
        This function has the role to get all meetings after an idMeet
        Parameters
        ----------
        hostId : Integer
            It is used for searching a meet after an hostId id.        
        """    
        self.cursor.execute(comands.selectIdMeetV, (hostId,))
        return self.cursor.fetchall()
    
    def selectMeetsByTime(self,  ora_begin, ora_end):
        """
        This function has the role to get all meetings from a specific
        date and hour interval.
        ----------
        ora_begin : str
            It is used for searching a meet which starts after ora_begin
        ora_begin : str
            It is used for searching a meet which starts before ora_end

        """    
        self.cursor.execute(comands.selectAllMeets, (ora_begin, ora_end))
        return self.cursor.fetchall()

    def createMeet(self,creator_id, ora_begin, ora_end):
        """
        This function has the role to create a meeting from a specific
        date and hour interval and with a host with creator_id
        ----------
        creator_id : Integer
            It is used for chosing a host_id 
        ora_begin : str
            It is used for creating a meet which starts after ora_begin
        ora_begin : str
            It is used for creating a meet which starts before ora_end
        """

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
        """
        This function has the role to delete a meeting and all invitations
        with a specific meet id.
        ----------
        meeting_id : Integer
            It is used for chosing a meeting_id and then delete that meeting
            and invitations. 
        """ 

        try:
            self.cursor.execute(comands.deleteInviteID, (meeting_id,))
            self.cursor.execute(comands.deleteMeetID, (meeting_id,))
            self.connection.commit()
        except Exception as e:
            print("Error deleting meeting and invitations:", str(e))
            self.connection.rollback()

    def deleteInvitation(self, meeting_id, person_id):
        """
        This function has the role to delete an invitation
        with a specific meet id and a specific person id.
        ----------
        meeting_id : Integer
            It is used for chosing a meeting_id and then delete that meeting
        person_id : Integer
            It is used for chosing a person_id and then delete that meeting
        """

        try:
            self.cursor.execute(comands.deleteInviteMeetIDpersonID, (meeting_id, person_id))
            self.connection.commit()
            print('delete done')
        except Exception as e:
            print("Error deleting invitation:", str(e))
            self.connection.rollback()

    def getInvitationsByName(self, person_name):
        """
        This function has the role to get all invitation
        after username.
        ----------
        person_name : str
            It is used for chosing a invitations
        """

        self.cursor.execute(comands.allPersonInvites, (person_name, person_name))
        return self.cursor.fetchall()

    def getInvitationsByTime(self, specific_time):
        """
        This function has the role to get all invitation
        after username.
        ----------
        specific_time : str
            It is used for chosing a invitations after a specific time
        """

        self.cursor.execute(comands.allMeetInvites, (specific_time, specific_time))
        return self.cursor.fetchall()

    def getMeetsInvitationsById(self, id):
        """
        This function has the role to get all invitation  where
        user is invited or is host.
        after username.
        ----------
        id : Integer
            It is used for chosing an invitations after a specific id
        """

        self.cursor.execute(comands.allMeetInvById, (id, id))
        return self.cursor.fetchall()
    
    def getInvitationByIdUserAndIdMeet(self,idUser,idMeet):
        """
        This function has the role to get all invitation and all meetings where
        user is invited or is host.
        after username.
        ----------
        idUser : Integer
            It is used for chosing an invitations after a specific 
            idUser
        idMeet : Integer
            It is used for chosing an invitations after a specific 
            idMeet
        """
        self.cursor.execute(comands.InvitationByNameAndIdMeet, (idUser, idMeet))
        return self.cursor.fetchall()
        
    def addInvitation(self, meetingId, personId):
        """
        This function has the role to create an invitation
        if it doesn't aleready exists
        after username.
        ----------
        meetingId : Integer
            It is used for creating an invitations after a specific 
            idUser
        personId : Integer
            It is used for creating an invitations after a specific 
            idMeet
        """
        try:
            self.cursor.execute(comands.addInvite, (meetingId, personId))
            self.connection.commit()
        except Exception as e:
            print("Error adding invitation:", str(e))
            self.connection.rollback()
    
    def getMeetAfterId(self,meetingId):
        """
        This function has the role to get a meet
        if it doesn't aleready exists
        after a meetingId.
        ----------
        meetingId : Integer
            It is used for getting an meet after this id.
        """
        self.cursor.execute(comands.getMeetAfterId, (meetingId,))
        return self.cursor.fetchall()
    
    def getInvitations(self,username): #fol asta
        """
        This function has the role to get all invitations
        where my user has that username
        after a meetingId.
        ----------
        username : str
            It is used for getting an invitation after a user username
        """
        self.cursor.execute(comands.getMeetYouInvited,(username,))
        return self.cursor.fetchall()

    def meetingExists(self,meeting_id, user_id):
        """
        This function has the role to verify if that meeting exists
        ----------
        meeting_id : Integer
            It is used for verifing existance meeting process --> (meeting_id, user_id)
        user_id : Integer
            It is used for verifing existance meeting process --> (meeting_id, user_id)
        """
        self.cursor.execute(comands.meetExists,(meeting_id, user_id))
        return self.cursor.fetchall()
    
    def invitationExists(self,meeting_id, user_id):
        """
        This function has the role to verify if that invitation exists
        ----------
        meeting_id : Integer
            It is used for verifing existance invitation process --> (meeting_id, user_id)
        user_id : Integer
            It is used for verifing existance invitation process --> (meeting_id, user_id)
        """

        self.cursor.execute(comands.invitationExists,(meeting_id, user_id))
        return self.cursor.fetchall()       

    def createInvitation(self,meeting_id, user_id):
        """
        This function has the role to create an invitation for a
        specific meeting_id and user_id
        ----------
        meeting_id : Integer
            It is used for creating an invite
        user_id : Integer
            It is used for creating an invite
        """

        try:
            self.cursor.execute(comands.addInvite, (meeting_id, user_id))
            self.connection.commit()
            return True
        except Exception as e:
            print("Error creating invitation:", str(e))
            self.connection.rollback()
            return None                  
        
    def createMeetImport(self,meet_id,creator_id, ora_begin, ora_end):
        """
        This function has the role to create a meeting from a specific
        date and hour interval and with a host with creator_id from an
        import file.
        ----------
        creator_id : Integer
            It is used for chosing a host_id 
        ora_begin : str
            It is used for creating a meet which starts after ora_begin
        ora_begin : str
            It is used for creating a meet which starts before ora_end
        """
        try:
            self.cursor.execute(comands.addMeetV, (meet_id,creator_id, ora_begin, ora_end))
            meetId = self.cursor.fetchone()[0]
            self.connection.commit()
            return meetId
        except Exception as e:
            print("Error creating meet:", str(e))
            self.connection.rollback()
            return None
    
    def invitationExistsMeetID(self,meetID):
        """
        This function has the role to verify if that invitation exists after a meetId
        ----------
        meeting_id : Integer
            It is used for verifing existance invitation process --> meeting_id
        """

        self.cursor.execute(comands.existsMeetID,(meetID,))
        return self.cursor.fetchall()
    
    def deleteInvitationMeetID(self,meetID):
        """
        This function has the role to delete invitations with that meetId
        ----------
        meeting_id : Integer
            It is used for deleting invitation process --> meeting_id
        """

        try:
            self.cursor.execute(comands.deleteInvMeetID,(meetID,))
            self.connection.commit()
            print('delete done')
        except Exception as e:
            print("Error deleting invitation:", str(e))
            self.connection.rollback()
    
    def deleteMeetJustID(self,meetID):
        """
        This function has the role to delete a meet with that meetId
        ----------
        meeting_id : Integer
            It is used for delete meet process --> meeting_id
        """

        try:
            self.cursor.execute(comands.deleteMeetID,(meetID,))
            self.connection.commit()
            print('delete done')
        except Exception as e:
            print("Error deleting invitation:", str(e))
            self.connection.rollback()
    
    def searchInvitaion(self,idUser):
        """
        This function has the role to get all invitations
        where my user idUser
        ----------
        idUser : Integer
            It is used for getting an invitation after a user idUser
        """
        self.cursor.execute(comands.getMeetYouInvited,(idUser,))
        return self.cursor.fetchall()