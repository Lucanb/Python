import sys
import db.handler.personsManagement as persons
import db.handler.meetings_maagement as meetings
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class DeletePersonWindow(QWidget):
    """
    A class that represents a window which will be showed and will have a
    QLineEdit element for id of meet,a QLineEdit for username that I want 
    to verify if that invite exits and delete it for that a user to be deleted
    from a meeting.
    ...

    Atributes
    ---------
    username : str
        It represents our username and it is used too see what for wich meeting
        I am a host so I have permission to delete an invited user.
    Methods
    -------
    def initUI():
        Represents a function that creates our window object and activates it and
        will offer us the interface made by 2 QLineEdit el -- >username that I want 
        to delete and the meet id from where I want to delete the user and a 
        QPushButton for starting executing this operation.
    def deletePerson():
        Represents a function that use person management class for getting my Id
        which is a host Id and a meeting management class for verify that id meet 
        exists then verify that I am a host and display  and then verifying that
        user exists and then if invite exits it will delete it.
    """

    def __init__(self,username):
        """
        Constructs all the necessary attributes for creating a window class
        with wigets that helps me to delete an invited person from a meet.

        Parameters
        ----------
        username : str
            Is used for getting my id and then verify if I am a host
            of a meet that I want to delete a person from it.
        """

        self.username = username
        super().__init__()
        self.initUI()
    
    def initUI(self):
        """
        Constructs all the necessary attributes for delete a user from a meet window.
        It will have a QLineEdit element for id of meet,a QLineEdit for username that I want 
        to verify if that invite exits and delete it for that a user to be deleted
        from a meeting

        Parameters
        ----------
        """

        self.setWindowTitle('Delete Person')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.usernameLineEdit = QLineEdit(self)
        self.usernameLineEdit.setPlaceholderText('Username Delete')
        layout.addWidget(self.usernameLineEdit)

        self.meetIDLineEdit = QLineEdit(self)
        self.meetIDLineEdit.setPlaceholderText('ID meet')
        layout.addWidget(self.meetIDLineEdit)

        self.okButton = QPushButton('OK', self)
        self.okButton.clicked.connect(self.deletePerson)
        layout.addWidget(self.okButton)

        self.setLayout(layout)

    def deletePerson(self):
        """
        A function that use meetings management class and person management 
        class for getting my Id which is a host Id and a meeting management 
        class for verify that id meet exists then verify that I am a host 
        and display  and then verifying that user exists and then if invite 
        exits it will delete it.If will show a QMesssageBox where it will 
        say if the operations is done or not.
        Parameters
        ----------
        """   

        myAccount = persons.PersonManagement()
        meets = meetings.MeetingManagement()   
        try:
            meetingId = self.meetIDLineEdit.text()
            username = self.usernameLineEdit.text()
            myID = myAccount.getUserId(self.username)
            print(myID)
            userID = myAccount.getUserId(username)
            print(userID)
            isHost = meets.meetingExists(meetingId,myID)
            print(isHost)
            if isHost:    
                inviteIsVAlid = meets.invitationExists(meetingId,userID)
                print(inviteIsVAlid)
                if inviteIsVAlid:
                    meets.deleteInvitation(userID,meetingId)
                    QMessageBox.information(self, 'Success', 'Person successfully deleted')  
                else:
                    QMessageBox.information(self, 'Failure', 'Person not Invited')
            else:
                QMessageBox.information(self, 'Failure', 'Person is not host of that meeting')             
        except Exception as e:
            QMessageBox.warning(self, 'Error', 'Failed to delete person')
            print(f"Error: {e}")
            return