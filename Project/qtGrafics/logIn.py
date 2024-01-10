import sys
from pathlib import Path
import db.handler.AccountsManagement as accounts
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton,QHBoxLayout, QVBoxLayout,QMessageBox
import controlPanel as control
import createAccount as create

class LogIn(QWidget):
    """
    A class that represents my login window
    
    ...

    Atributes
    ---------
    window : class
        A class that have my application control panel for a user operations
    createAccountWindow : class
        A class that represents a window for creeating my account
    username : QLineEdit
        A QLineEdit widget for entering a text that represent a username
    password : QLineEdit
        A QLineEdit widget for entering the password text
    loginButton : QPushButton
        A QPushButton for starting the login operation by using LoginButton function
    createAccountButton : QPushButton
        A QPushButton for opening the creating account window
    
    Methods
    -------
    def initUI():
        Is activated at object initialisation and it gives me the necesary interface for my window
    def LoginButton():
        Is activated when I press loginButton and verify if 
        my user exists in accountUsers tabel then if it exists 
        a QMessageBox will appear with succes logged message and then
        the user will be redirected to control panel window, else it
        will ramian on login window and will appear a failure login 
        window
    def CreateAccButton():
        Is activated when I press createAccountButton and shows us 
        a create account window.
    """
    
    def __init__(self):
        """
        Constructs all the necessary attributes for the login window object.

        Parameters
        ----------
        """
                
        super().__init__()
        self.initUI()
        self.window = None
        self.createAccountWindow = None
    
    def initUI(self):
        """
        Constructs all the necessary attributes for my login window interface.

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

        self.loginButton = QPushButton('Login', self)
        self.loginButton.clicked.connect(self.LoginButton)

        self.createAccountButton = QPushButton('Create Account', self)
        self.createAccountButton.clicked.connect(self.CreateAccButton)

        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.loginButton)
        layout.addWidget(self.createAccountButton)
        layout.addStretch(1)
        self.setLayout(layout)

    def LoginButton(self):
        """
        It verify if my login user text(username,password) from textboxes 
        are in my accountusers and if are there it will show a QMessageBox 
        with succes login message and redirect us to control panel else
        it will just show a QMessageBox with login failure.

        Parameters
        ----------
        """

        myAccount = accounts.AccountsManagementt()
        msg = QMessageBox()
        username = self.username.text()
        password = self.password.text()
        isAccount = myAccount.verifyLogIn(username,password)
        print("Username:", username)
        print("Password:", password)
        msg.setText('Login successful' if isAccount else 'Login failed')
        msg.exec_()  
        if isAccount == True:
            print('User Loggend Successful')
            if not self.window:
                self.window = control.Window(username)
            self.window.show()
            self.close() 
        else:
            print('User logged failed')
    
    def CreateAccButton(self):
        """
        Construct the necesary window for creeating my account class and shows
        it on the screen.

        Parameters
        ----------
        """

        if not self.createAccountWindow:
            self.createAccountWindow = create.CreateAccount()
        self.createAccountWindow.show()        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginWindow = LogIn()
    loginWindow.show()
    sys.exit(app.exec_())

    
