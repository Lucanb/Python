import sys
import db.handler.personsManagement as persons
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class AddPersonWindow(QWidget):
    """
    A class that represents add person window and it
    has buttons for username,first name,last name and password.
    It olso has an oke button and if informations are oke,the 
    user will be added in my database.Else it will show a QMessageBox
    with failure.
    
    ...

    Atributes
    ---------
    usernameLineEdit : QLineEdit
        A QLineEdit widget where I can indroduce a username.
    passwordLineEdit : QLineEdit
        A QLineEdit widget where I can indroduce a password.
    firstnameLineEdit : QLineEdit
        A QLineEdit widget for entering a text that represent first name.
    lastnameLineEdit : QLineEdit
        A QLineEdit widget for entering the last name text
    okButton : QPushButton
        A QPushButton for starting the add person operation by using addPerson() function
    
    Methods
    -------
    def initUI():
        Is activated at object initialisation and it gives me the necesary interface for my window
        like QLineEdit camps a QPushButton that activate function addPerson().

    def addPerson():
        This function is used when I pressed addPerson button and it insert in my
        data base the data I introduced in form window if they are valid.It will
        show a QMessageBox with corresponding message.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the addPersonWindow window object.

        Parameters
        ----------
        """

        super().__init__()
        self.initUI()
    
    def initUI(self):
        """
        Constructs all the necessary attributes for my AddPersonWIndow window interface.
        There are 4 QLineEdit widgets and a QPushButton widget which is activated by
        addPerson() function.

        Parameters
        ----------
        """

        self.setWindowTitle('Add Person')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.usernameLineEdit = QLineEdit(self)
        self.usernameLineEdit.setPlaceholderText('Username')
        layout.addWidget(self.usernameLineEdit)

        self.passwordLineEdit = QLineEdit(self)
        self.passwordLineEdit.setPlaceholderText('Password')
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.passwordLineEdit)

        self.firstnameLineEdit = QLineEdit(self)
        self.firstnameLineEdit.setPlaceholderText('FirstName')
        layout.addWidget(self.firstnameLineEdit)

        self.lastnameLineEdit = QLineEdit(self)
        self.lastnameLineEdit.setPlaceholderText('LastName')
        layout.addWidget(self.lastnameLineEdit)

        self.okButton = QPushButton('OK', self)
        self.okButton.clicked.connect(self.addPerson)
        layout.addWidget(self.okButton)

        self.setLayout(layout)

    def addPerson(self):
        """
        This function is activate when we click a button and the it takes my 
        text from widgets and verify if datas are valid and then it inserts them
        into my database with addUser function from myAccount class.

        Parameters
        ----------
        button : QPushButton
        It represents a button from my control panel window.
        """

        myAccount = persons.PersonManagement()
        msg = QMessageBox()
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        firstname= self.firstnameLineEdit.text()
        lastname = self.lastnameLineEdit.text()       
        try:
            isAccountValid = myAccount.addUser(username,password,firstname,lastname)
            print("Username:", username)
            print("Password:", password)            
            QMessageBox.information(self, 'Success', 'Person successfully added')           
        except Exception as e:
            QMessageBox.warning(self, 'Error', 'Failed to add person')
            print(f"Error: {e}")
            