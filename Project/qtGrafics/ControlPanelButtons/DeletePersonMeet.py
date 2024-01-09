import sys
import db.handler.personsManagement as persons
import db.handler.meetings_maagement as meetings
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class DeletePersonWindow(QWidget):
    def __init__(self,username):
        self.username = username
        super().__init__()
        self.initUI()
    
    def initUI(self):
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
        myAccount = persons.PersonManagement()
        meets = meetings.MeetingManagement()   
        try:
            # scot id-ul persoanei,dupa verific daca sunt host pentru acel meet(daca da ma duc sa vad daca pesoana se afla in invitatii si sterg invitatia lui)
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