import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox,QScrollArea
import ControlPanelButtons.ResultsWindow as resW
import db.handler.meetings_maagement as meetings
import db.handler.personsManagement as person

class SearchInvitations(QWidget):
    def __init__(self):
        super().__init__()
        self.resultsWindow = None
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Search Persons')
        layout = QVBoxLayout()

        self.userNameLabel = QLabel('userName')
        self.userNameInput = QLineEdit()

        self.okButton = QPushButton('OK')
        self.okButton.clicked.connect(self.selectTimes)

        layout.addWidget(self.userNameLabel)
        layout.addWidget(self.userNameInput)

        layout.addWidget(self.okButton)

        self.setLayout(layout)


    def selectTimes(self):
        userName = self.userNameLabel.text()
        try:
            meeting = meetings.MeetingManagement()
            persons = person.PersonManagement()
            # idUser = persons.getUserId(userName)
            idUser =16
            print(idUser)
            if idUser:
                results = meeting.searchInvitaion(idUser)
                print(results)
                if self.resultsWindow is not None:
                    self.resultsWindow.close()
                self.resultsWindow = resW.ResultsWindow(results)
                self.resultsWindow.show()
            else:
                QMessageBox.information(self, 'Failure', 'Id does not exists')
        except Exception as error_selectingDb:
            QMessageBox.warning(self, 'Error', str(error_selectingDb))
