from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QLabel, QMessageBox)
import db.handler.meetings_maagement as meetings
import db.handler.personsManagement as person
class addMeetings(QWidget):
    def __init__(self,username):
        super().__init__()
        self.hostName = username
        self.userInputs = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Add Meetings')
        self.setGeometry(100, 100, 500, 500)

        layout = QVBoxLayout()
        self.beginDate = QLineEdit(self)
        self.beginDate.setPlaceholderText('Data de început (YYYY-MM-DD)')
        layout.addWidget(self.beginDate)

        self.beginTime = QLineEdit(self)
        self.beginTime.setPlaceholderText('Ora de început (HH:MM:SS)')
        layout.addWidget(self.beginTime)

        self.endDate = QLineEdit(self)
        self.endDate.setPlaceholderText('Data de sfarsit (YYYY-MM-DD)')
        layout.addWidget(self.endDate)

        self.endTime = QLineEdit(self)
        self.endTime.setPlaceholderText('Ora de sfarsit (HH:MM:SS)')
        layout.addWidget(self.endTime)

        self.usersLayout = QVBoxLayout()
        layout.addLayout(self.usersLayout)
        self.addUserToMeet()

        addUserButton = QPushButton('Adauga Utilizator', self)
        addUserButton.clicked.connect(self.addUserToMeet)
        layout.addWidget(addUserButton)

        deleteUserButton = QPushButton('Sterge utilizator', self)
        deleteUserButton.clicked.connect(self.deleteUserToMeet)
        layout.addWidget(deleteUserButton)

        validButton = QPushButton('Trimite', self)
        validButton.clicked.connect(self.submitData)
        layout.addWidget(validButton)
        
        self.setLayout(layout)    

    def addUserToMeet(self):
        userName = QLineEdit(self)
        userName.setPlaceholderText('Nume utilizator')
        self.usersLayout.addWidget(userName)
        self.userInputs.append(userName)

    def deleteUserToMeet(self):
        if self.userInputs:
            userEdit = self.userInputs.pop()
            userEdit.deleteLater()


    def submitData(self):
        hour_begin = f"{self.beginDate.text()} {self.beginTime.text()}:00+03"
        hour_end = f"{self.endDate.text()} {self.endTime.text()}:00+03"
        usernames = [userInput.text() for userInput in self.userInputs if userInput.text()]
        user = person.PersonManagement()
        hostId = user.getUserId(self.hostName)
        print(hostId)
        meetMangement = meetings.MeetingManagement()
        idMeet = meetMangement.createMeet(hostId,hour_begin,hour_end)
        for username in usernames:
            userId = user.getUserId(username)
            meetMangement.addInvitation(idMeet,userId)

        QMessageBox.information(self, 'Informatie', 'Datele au fost trimise.')    