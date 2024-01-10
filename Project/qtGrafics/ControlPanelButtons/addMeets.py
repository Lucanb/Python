from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton, 
                             QVBoxLayout, QHBoxLayout,QScrollArea, QLabel, QMessageBox)
import db.handler.meetings_maagement as meetings
import db.handler.personsManagement as person
class addMeetings(QWidget):
    """
    A class that represents add meeting window and it
    has QLineEdit for beginDate,endDate,beginHour,endHour,addUser and
    QPushButtons for add a new user to meet,delete user and OK button
    and  if informations are ok,the meet and invitations will be added in my 
    database.Else it will show a QMessageBox with failure.
    
    ...

    Atributes
    ---------
    hostName : str
        It has the username of the user who creates a meet and it will add
        him as a host when the meet is created.
    userInputs : list
        Is a list with usernames of users that I want to invite in meet,those
        users will be added by inserting invitations.
    beginDate : QLineEdit
        A QLineEdit widget where I can indroduce the begining meeting date.
    endDate : QLineEdit
        A QLineEdit widget for entering a text that represent ending meeting date.
    beginTime : QLineEdit
        A QLineEdit widget for entering the meeting begining hour.
    endTime : QLineEdit
        A QLineEdit widget for entering the meeting ending hour.
    addUserButton : QPushButton
        A QPushButton for adding a user into my container.
    deleteUserButton : QPushButton
        A QPushButton for deleting a user from my container.
    validButton : QPushButton
        A QPushButton for starting the add person operation by using addPerson() function.
    
    Methods
    -------
    def initUI():
        Is activated at object initialisation and it gives me the necesary interface for my window
        like QLineEdit camps and many QPushButton for adding,deleting my user and sending informations
        to submitData function which will insert the meeting and invites.
    def addUserToMeet():
        This function is used when I pressed addPerson button and it will insert a new username into
        my userInputs list.
    def deleteUserToMeet():
        This function is used when I pressed addPerson button and it will delete last username from
        my userInputs list.
    def submitData():
        This function is used when I pressed submit button and it will create my invitations and my meeting.
    """

    def __init__(self,username):
        """
        Constructs all the necessary attributes for the addMeets window object.

        Parameters
        ----------
        hostName :
            Represents the name of the user that creates the meet.
        userInputs :
            Reoresents a list of usernames that will be usefull when I want to create invitations
            for my users.    
        """

        super().__init__()
        self.hostName = username
        self.userInputs = []
        self.initUI()

    def initUI(self):
        """
        Constructs all the necessary attributes for my AddPersonWIndow window interface.
        There are 4 QLineEdit widgets and many QPushButton for adding,deleting my user 
        and sending informations to submitData function which will insert the meeting 
        and invites

        Parameters
        ----------
        """

        self.setWindowTitle('Add Meetings')
        self.setGeometry(100, 100, 500, 500)

        layout = QVBoxLayout()

        self.beginDate = QLineEdit(self)
        self.beginDate.setPlaceholderText('Data de început (YYYY-MM-DD)')
        layout.addWidget(self.beginDate)

        self.beginTime = QLineEdit(self)
        self.beginTime.setPlaceholderText('Ora de început (HH:MM:SS)')
        layout.addWidget(self.beginTime)

        self.endDate = QLineEdit(self)
        self.endDate.setPlaceholderText('Data de sfarsit (YYYY-MM-DD)')
        layout.addWidget(self.endDate)

        self.endTime = QLineEdit(self)
        self.endTime.setPlaceholderText('Ora de sfarsit (HH:MM:SS)')
        layout.addWidget(self.endTime)

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
        This function is activate when we click a addUser button and
        it will add a new user to my container and then to my user list
        for creating invites when submit button in pressed.

        Parameters
        ----------
        """

        userName = QLineEdit(self)
        userName.setPlaceholderText('Nume utilizator')
        self.usersLayout.addWidget(userName)
        self.userInputs.append(userName)

    def deleteUserToMeet(self):
        """
        This function is activate when we click a addUser button and
        it will delete a user to my container and then to my user list
        for creating invites when submit button in pressed.

        Parameters
        ----------
        """
        if self.userInputs:
            userEdit = self.userInputs.pop()
            userEdit.deleteLater()


    def submitData(self):
        """
        This function is activate when I press submit button and it will
        tconstruct our 2 datas for begining and endig the meet and then it
        will create a meet and then it will got in user name list and add
        invitations for users.

        Parameters
        ----------
        """

        hour_begin = f"{self.beginDate.text()} {self.beginTime.text()}:00+02"
        hour_end = f"{self.endDate.text()} {self.endTime.text()}:00+02"
        usernames = [userInput.text() for userInput in self.userInputs if userInput.text()]
        user = person.PersonManagement()
        try:        
            hostId = user.getUserId(self.hostName)
            print('host_id -> getUserId : ',hostId)
            meetMangement = meetings.MeetingManagement()
            idMeet = meetMangement.createMeet(hostId,hour_begin,hour_end)
            print('id-ul meet-ului este',idMeet)
            for username in usernames:
                userId = user.getUserId(username)
                if userId :
                    meetMangement.addInvitation(idMeet,userId)
                else:
                    QMessageBox.information(self, 'No user added', f'Acest username nu exista {username}')
        except Exception as error:
            QMessageBox.warning(self, 'Eroare', 'Eroare la creearea meeting-ului')
            print(f"Error: {error}") 
        QMessageBox.information(self, 'Informatie', 'Datele au fost trimise.')    