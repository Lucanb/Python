from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton, 
                             QVBoxLayout, QHBoxLayout,QScrollArea, QLabel, QMessageBox)
import db.handler.meetings_maagement as meetings
import db.handler.personsManagement as person

class addPersonToMeet(QWidget):
    def __init__(self,username):
        super().__init__()
        self.hostName = username
        self.userInputs = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Add Meetings')
        self.setGeometry(100, 100, 500, 500)

        layout = QVBoxLayout()

        self.idMeet = QLineEdit(self)
        self.idMeet.setPlaceholderText('Meet ID')
        layout.addWidget(self.idMeet)

        scrollBar = QScrollArea(self)
        scrollBar.setWidgetResizable(True)
        userContainer = QWidget()
        self.usersLayout = QVBoxLayout(userContainer)
        scrollBar.setWidget(userContainer)
        layout.addWidget(scrollBar)

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
        meet_id = self.idMeet.text()
        usernames = [userInput.text() for userInput in self.userInputs if userInput.text()]
        user = person.PersonManagement()
        hostId = user.getUserId(self.hostName)
        print('host_id -> getUserId:', hostId)
        meetManagement = meetings.MeetingManagement()
        rows_meet = meetManagement.getMeetAfterId(meet_id)
        if not rows_meet:
            QMessageBox.warning(self, 'Avertizare', 'Meet-ul ' + meet_id + ' nu exista')
        else: 
            print('id-ul meet-ului este', meet_id)
            for username in usernames:
                userId = user.getUserId(username)
                if userId is not None:                
                    rows = meetManagement.getInvitationByIdUserAndIdMeet(userId, meet_id)
                    print(rows)
                    if rows:
                        QMessageBox.warning(self, 'Avertizare', 'Utilizatorul ' + username + ' are deja o invitație pentru acest eveniment.')
                    else:
                        meetManagement.addInvitation(meet_id, userId)
                        QMessageBox.information(self, 'Informație', 'Datele au fost trimise.')
                else:
                    QMessageBox.warning(self, 'Avertizare', 'Utilizatorul ' + username + ' nu există în baza de date.')
    