import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox,QScrollArea
import ControlPanelButtons.ResultsWindow as resW
import db.handler.personsManagement as person

class SearchPersons(QWidget):
    def __init__(self):
        super().__init__()
        self.resultsWindow = None
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Search Persons')
        layout = QVBoxLayout()

        self.lastNameLabel = QLabel('Nume:')
        self.lastNameInput = QLineEdit()
        self.firstNameLabel = QLabel('Prenume:')
        self.firstNameInput = QLineEdit()

        self.okButton = QPushButton('OK')
        self.okButton.clicked.connect(self.selectTimes)

        layout.addWidget(self.lastNameLabel)
        layout.addWidget(self.lastNameInput)
        layout.addWidget(self.firstNameLabel)
        layout.addWidget(self.firstNameInput)
        layout.addWidget(self.okButton)

        self.setLayout(layout)


    def selectTimes(self):
        lastName = self.lastNameInput.text()
        firstName = self.firstNameInput.text()
        try:
            user = person.PersonManagement()
            results = user.searchPerson(firstName,lastName)
            print(results)
            if self.resultsWindow is not None:
                self.resultsWindow.close()
            self.resultsWindow = resW.ResultsWindow(results)
            self.resultsWindow.show()
        except Exception as error_selectingDb:
            QMessageBox.warning(self, 'Error', str(error_selectingDb))
