import sys
import db.handler.personsManagement as persons
import db.handler.meetings_maagement as meetings
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class DeleteMeet(QWidget):
    def __init__(self,username):
        self.username = username
        super().__init__()
        self.initUI()
    
    def initUI(self):
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
        myAccount = persons.PersonManagement()
        meets = meetings.MeetingManagement()   
        try:
            # scot id-ul persoanei,dupa verific daca sunt host pentru acel meet(daca da ma duc sa vad daca pesoana se afla in invitatii si sterg invitatia lui)
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