import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox,QScrollArea
import ControlPanelButtons.ResultsWindow as resW
import db.handler.personsManagement as person

class SearchPersons(QWidget):
    """
    A class that represents a window which shows a window from where I can 
    insert an in QLineEdit elements first name and last name  and then it will show 
    a window with al db persons searched.
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
        using a person and it will save select results and then put them in my window.
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
        Constructs all the necessary attributes for building a search person window.
        It will have 2 QLineEdit element for inserting a firstname and lastname and a QPushButton
        for activate select Time function which will create a window with all names.

        Parameters
        ----------
        """

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
        """
        A function that use person management class
        for accesing the necesary data from my database and then creating a new
        resultsWindow class that will be added to curent class argument and that will
        show my results.

        Parameters
        ----------
        """

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
