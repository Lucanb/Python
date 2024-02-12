import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox,QScrollArea
import ControlPanelButtons.ResultsWindow as resW
import db.handler.meetings_maagement as meetings
import db.handler.personsManagement as person

class SearchInvitations(QWidget):
    """
    A class that represents a window which shows a window from where I can 
    insert an idUser and then I can show a window with al db invites elemnts.
    ...

    Atributes
    ---------
    resultsWindow : class
        It is initialised with none but it will represent a window class where all
        invites will be showed.
    Methods
    -------
    def selectTimes():
        Represents a function that creates our window object and activates it and that
        using a person and a meting manager it will save select results and then put them
        in my window.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for selecting necesay data and then 
        displaying it in a new window class.

        Parameters
        ----------
        """

        super().__init__()
        self.resultsWindow = None
        self.initUI()

    def initUI(self):
        """
        Constructs all the necessary attributes for building a search invitation window.
        It will have a QLineEdit element for inserting a username and a QPushButton
        for activate select Time function which will create a window with all invitations
        for a user name.

        Parameters
        ----------
        """

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
        """
        A function that use meetings management class and person management class
        for accesing the necesary data from my database and then creating a new
        resultsWindow class that will be added to curent class argument and that will
        show my results.

        Parameters
        ----------
        """
        
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
