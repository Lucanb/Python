import sys
import db.handler.AccountsManagement as accounts
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton,QHBoxLayout, QVBoxLayout,QMessageBox

class CreateAccount(QWidget):
    """
    for test
    """
    def __init__(self):
        super().__init__()
        self.initUI()
    

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
