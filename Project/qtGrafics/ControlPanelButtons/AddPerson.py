import sys
import db.handler.personsManagement as persons
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class AddPersonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
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
            