import sys
import db.handler.personsManagement as persons
import db.handler.meetings_maagement as meetings
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class DeleteMeet(QWidget):
    """
    A class that represents a window which will be showed and will have a
    QLineEdit element for id of meet that I want to delete and a QpushButton
    that will activate a delete meeting function.
    ...

    Atributes
    ---------
    username : str
        It represents our username and it is used too see what for wich meeting
        I am a host so I have permission to delete.
    Methods
    -------
    def initUI():
        Represents a function that creates our window object and activates it and
        will offer us the interface made by a QLineEdit element and a QPushButton
        element for deleting a meet.
    def deleteMeeting():
        Represents a function that use person management class for getting my Id
        which is a host Id and a meeting management class for verify that id meet 
        exists then verify that I am a host and display succes if it can delete all
        meet invitations and my meet.
    """

    def __init__(self,username):
        """
        Constructs all the necessary attributes for creating a window class
        with wigets that helps me to delete a meeting.

        Parameters
        ----------
        username : str
            Is used for getting my id and then verify if I am a host
            of ameet that I want to delete.
        """

        self.username = username
        super().__init__()
        self.initUI()
    
    def initUI(self):
        """
        Constructs all the necessary attributes for my delete meet window.
        One QLineEdit for meetingID and one QPushButton(OK) for activate
        deleteMeeting function.

        Parameters
        ----------
        """

        self.setWindowTitle('Delete Meeting')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.meetIDLineEdit = QLineEdit(self)
        self.meetIDLineEdit.setPlaceholderText('ID meet')
        layout.addWidget(self.meetIDLineEdit)

        self.okButton = QPushButton('OK', self)
        self.okButton.clicked.connect(self.deleteMeeting)
        layout.addWidget(self.okButton)

        self.setLayout(layout)

    def deleteMeeting(self):
        """
        A function that use meetings management class and person management class
        for verifing that my meet id exists in data base and the if I am a host.If
        this is oke,we will verify if there are invites for other users and delete them,
        after that we cand delete our meeting.A QMessageBox will tell us if this operation
        has been done ore not.

        Parameters
        ----------
        """        
        myAccount = persons.PersonManagement()
        meets = meetings.MeetingManagement()   
        try:
            meetingId = self.meetIDLineEdit.text()
            myID = myAccount.getUserId(self.username)
            print(myID)
            isHost = meets.meetingExists(meetingId,myID)
            print(isHost)
            if isHost:    
                inviteIsVAlid = meets.invitationExistsMeetID(meetingId)
                print(inviteIsVAlid)
                if inviteIsVAlid:
                    meets.deleteInvitationMeetID(meetingId)
                    QMessageBox.information(self, 'Success', 'Invitations successfully deleted')  
                meets.deleteMeetJustID(meetingId) 
                QMessageBox.information(self, 'Success', 'Meeting successfully deleted')   
            else:
                QMessageBox.information(self, 'Failure', 'Person is not host of that meeting')             
        except Exception as e:
            QMessageBox.warning(self, 'Error', 'Failed to delete person')
            print(f"Error: {e}")
            return