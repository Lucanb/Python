import sys
import db.handler.AccountsManagement as accounts
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton,QHBoxLayout, QVBoxLayout,QMessageBox

class CreateAccount(QWidget):
    """
    A class that represents my create account window
    
    ...

    Atributes
    ---------
    username : QLineEdit
        A QLineEdit widget for entering a text that represent a username
    password : QLineEdit
        A QLineEdit widget for entering the password text
    confirmPassword : QLineEdit
        A QLineEdit widget for entering the confirm password text
    firstName : QLineEdit
        A QLineEdit widget for entering the first name text
    lastName : QLineEdit
        A QLineEdit widget for entering the last name text
    createAccountButton : QPushButton
        This button activates CreateAccButton function for adding my form data into database -->
        accountusers table if it doesn't exits yet
    
    Methods
    -------
    def initUI():
        Is activated at object initialisation and it gives me the necesary interface for my window
    def createAccountButton():
        This function is used for adding a user in my database --> accountusers table if they don't
        exists yet and the data are valid and then will open a QMessageBox window and tell us that
        they have been added.Else it will open a QMessageBox window and tell us that they cannot be added.
    """
    def __init__(self):
        """
        Initialise all the necessary attributes for the adding a new user in our 
        database(creating an account).

        Parameters
        ----------
        """
        super().__init__()
        self.initUI()
    

    def initUI(self):
        """
        Constructs all the necessary attributes for the creating account window object.

        Parameters
        ----------
        """
                
        self.setWindowTitle('MeetingScheduler')
        self.setGeometry(100, 100, 500, 900)

        self.username = QLineEdit(self)
        self.username.setPlaceholderText('Username')
        self.username.setFixedWidth(200)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText('Password')
        self.password.setFixedWidth(200)
        self.password.setEchoMode(QLineEdit.Password)

        self.confirmPassword = QLineEdit(self)
        self.confirmPassword.setPlaceholderText('Confirm password')
        self.confirmPassword.setFixedWidth(200)
        self.confirmPassword.setEchoMode(QLineEdit.Password)

        self.firstName = QLineEdit(self)
        self.firstName.setPlaceholderText('First Name')
        self.firstName.setFixedWidth(200)

        self.lastName = QLineEdit(self)
        self.lastName.setPlaceholderText('Last Name')
        self.lastName.setFixedWidth(200)

        self.createAccountButton = QPushButton('Create Account', self)
        self.createAccountButton.clicked.connect(self.CreateAccButton)

        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.confirmPassword)
        layout.addWidget(self.confirmPassword)
        layout.addWidget(self.firstName)
        layout.addWidget(self.lastName)
        layout.addWidget(self.createAccountButton)
        layout.addStretch(1)
        self.setLayout(layout)

    def CreateAccButton(self):
        """
        It verify if a username exists in our database and if it not then it will
        add it only if confirm password is the same as password.It will show a
        QMessageBox with message succes creating account if the upper condition is
        satisfied or failure creating user in other cases.

        Parameters
        ----------
        """

        myAccount = accounts.AccountsManagementt()
        msg = QMessageBox()
        username = self.username.text()
        password = self.password.text()
        confirmPass = self.confirmPassword.text()
        firstName = self.firstName.text()
        lastName  = self.lastName.text()
        if confirmPass != password :
            msg.setText('pasword must be the same as confirm password')
        else :
            isAccountValid = myAccount.CreateAccount(username,password,firstName,lastName)
            print("Username:", username)
            print("Password:", password)
            print("Confirmed Password",confirmPass)
            msg.setText('Account Created Succesfully!' if isAccountValid else 'Failed Creating Accont')
            msg.exec_()  
            if isAccountValid == True:
                print('Account Created Succesfully!')
            else:
                print('Failed Creating Accont')
