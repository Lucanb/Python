import sys
from pathlib import Path
import db.handler.AccountsManagement as accounts
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton,QHBoxLayout, QVBoxLayout,QMessageBox
import controlPanel as control
import createAccount as create

class LogIn(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.window = None
        self.createAccountWindow = None
    
    def initUI(self):

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
        layout.addStretch(1)
        self.setLayout(layout)

    def LoginButton(self):
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
                self.window = control.Window()
            self.window.show()
            self.close() 
        else:
            print('User logged failed')
    
    def CreateAccButton(self):
        if not self.createAccountWindow:
            self.createAccountWindow = create.CreateAccount()
        self.createAccountWindow.show()        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginWindow = LogIn()
    loginWindow.show()
    sys.exit(app.exec_())
