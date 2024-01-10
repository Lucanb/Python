from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton, 
                             QVBoxLayout, QHBoxLayout,QScrollArea, QLabel, QMessageBox)
import db.handler.meetings_maagement as meetings
import db.handler.personsManagement as person

class addPersonToMeet(QWidget):
    """
    A class that represents "add person to a specific meet" window and it
    has buttons for username,first name,last name and password.
    It olso has an oke button and if informations are oke,the 
    user will be added in my database.Else it will show a QMessageBox
    with failure.
    
    ...

    Atributes
    ---------
    hostName : str
        A string that represents our username and for which we want to create an invite for someone.
    userInputs : list
        A list which will have all usernames that we want to invite to our meeting.
    usernameLineEdit : QLineEdit
        A QLineEdit widget where I can indroduce a username for adding it to a meet.
    addUserButton : QPushButton
        A QPushButton widget where I can add another QLineText in my window for 
        adding a new username --> use function addUserToMeet().
    deleteUserButton : QPushButton
        A QPushButton widget where I can delete another QLineText in my window
        --> use function .
    validButton : QPushButton
        A QPushButton for starting the add person operation by using submitData()
        function deleteUserToMeet
    Methods
    -------
    def initUI(username):
        Is activated at object initialisation and it gives me the necesary interface for my window
        like QLineEdit camps a QPushButton that activate function addPerson().

    def addPerson():
        This function is used when I pressed addPerson button and it insert in my
        data base the data I introduced in form window if they are valid.It will
        show a QMessageBox with corresponding message.
    def addUserToMeet():
        This method is for adding a new user in mu userInputs list and adding
        a new QLineEdit camp.
    def deleteUserToMeet():
        This method is for deleting a user in mu userInputs listand and deleting
        a QLineEdit camp.
    def submitData():
        This method is for verifing if data are valid and then if it's oke inserting
        them into mai database in specific tables using managers objects.
    """


    def __init__(self,username):
        """
        Constructs all the necessary attributes for the addPersonWindow window object.

        Parameters
        ----------
        username : str
        Is used for verifing if I am the host of a meeting or when I want to add a
        person to a meet for sending invites.
        """

        super().__init__()
        self.hostName = username
        self.userInputs = []
        self.initUI()

    def initUI(self):
        """
        Constructs all the necessary attributes for my AddPersonToMeet window interface.
        There are n QLineEdit widgets from which one is my meetID , a QPushButton widget 
        which is activate addPerson() function,a widget which activate deletePerson()
        function and a QpushButton for submitting my datas.

        Parameters
        ----------
        """

        self.setWindowTitle('Add Meetings')
        self.setGeometry(100, 100, 500, 500)

        layout = QVBoxLayout()

        self.idMeet = QLineEdit(self)
        self.idMeet.setPlaceholderText('Meet ID')
        layout.addWidget(self.idMeet)

        scrollBar = QScrollArea(self)
        scrollBar.setWidgetResizable(True)
        userContainer = QWidget()
        self.usersLayout = QVBoxLayout(userContainer)
        scrollBar.setWidget(userContainer)
        layout.addWidget(scrollBar)

        addUserButton = QPushButton('Adauga Utilizator', self)
        addUserButton.clicked.connect(self.addUserToMeet)
        layout.addWidget(addUserButton)

        deleteUserButton = QPushButton('Sterge utilizator', self)
        deleteUserButton.clicked.connect(self.deleteUserToMeet)
        layout.addWidget(deleteUserButton)

        validButton = QPushButton('Trimite', self)
        validButton.clicked.connect(self.submitData)
        layout.addWidget(validButton)

        self.setLayout(layout)

    def addUserToMeet(self):
        """
        This function is activate when we click button addUser and the it 
        creates a newLineText widget where I can insert a new username

        Parameters
        ----------
        """

        userName = QLineEdit(self)
        userName.setPlaceholderText('Nume utilizator')
        self.usersLayout.addWidget(userName)
        self.userInputs.append(userName)

    def deleteUserToMeet(self):
        """
        This function is activate when we click button deleteUSer and the it 
        delete a newLineText widget.

        Parameters
        ----------
        """

        if self.userInputs:
            userEdit = self.userInputs.pop()
            userEdit.deleteLater()

    def submitData(self):
        """
        This function is activate when we click button submit and the it takes my 
        text from widgets and verify if datas are valid and then it inserts them
        into my database with person management class and meeting management class.

        Parameters
        ----------
        button : QPushButton
        It represents a button from my control panel window.
        """
        meet_id = self.idMeet.text()
        usernames = [userInput.text() for userInput in self.userInputs if userInput.text()]
        user = person.PersonManagement()
        try:
            hostId = user.getUserId(self.hostName)
            print('host_id -> getUserId:', hostId)
            meetManagement = meetings.MeetingManagement()
            rows_meet = meetManagement.getMeetAfterId(meet_id)
            if not rows_meet:
                QMessageBox.warning(self, 'Avertizare', 'Meet-ul ' + meet_id + ' nu exista')
            else: 
                print('id-ul meet-ului este', meet_id)
                for username in usernames:
                    userId = user.getUserId(username)
                    if userId is not None:                
                        rows = meetManagement.getInvitationByIdUserAndIdMeet(userId, meet_id)
                        print(rows)
                        if rows:
                            QMessageBox.warning(self, 'Avertizare', 'Utilizatorul ' + username + ' are deja o invitație pentru acest eveniment.')
                        else:
                            meetManagement.addInvitation(meet_id, userId)
                            QMessageBox.information(self, 'Informație', 'Datele au fost trimise.')
                    else:
                        QMessageBox.warning(self, 'Avertizare', 'Utilizatorul ' + username + ' nu există în baza de date.')
        except Exception as e:
            QMessageBox.warning(self, 'Error', 'Failed to add person')
            print(f"Error: {e}")
    