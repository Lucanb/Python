import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout,QLabel
from datetime import datetime
import ControlPanelButtons.AddPerson as person
import ControlPanelButtons.showMeetTimeWindow as showMeetTimes
import ControlPanelButtons.AllMeetsId as allMeetsId
import ControlPanelButtons.addMeets as addNewMeet
import ControlPanelButtons.addPersonToMeet as addPersToMeet
import ControlPanelButtons.ShowAllHostMeets as hostMeets
import ControlPanelButtons.SearchPersons as searchPers
import ControlPanelButtons.DeletePersonMeet as deletePersonFromMeet
import ControlPanelButtons.deleteMeet as deletMeets
import ControlPanelButtons.searchInvitationsWindow as searchInvWindow
import exportCalendar as exports
import importCalendar as imports

class Window(QWidget):
    """
    A class that represents my control panel window where I have
    differents buttons with differents functionalities.
    
    ...

    Atributes
    ---------
    window : class
        A class that have my application control panel for a user operations
    addPersonWindow : class
        A class that represents a window for creeating my account
    showAllMeetsWindow : QLineEdit
        A QLineEdit widget for entering a text that represent a username
    addPersonToMeetWindow : QLineEdit
        A QLineEdit widget for entering the password text
    addMeetWindow : QPushButton
        A QPushButton for starting the login operation by using LoginButton function
    showMeetTimeWindow : QPushButton
        A QPushButton for opening the creating account window
    exports :
    hostMeet :
    searchPersWindow :
    deletePersonWindowMeet :
    deleteAmeetWindow :
    searchInvitationsWindow :
    
    Methods
    -------
    def initUI():
        Is activated at object initialisation and it gives me the necesary interface for my window
    def onButtonClicked():
        This function indicates if I pressed a button from my control pannel and then it looks which
        button(after its name) was pressed and then executes the specify function which implements
        its desire.
    def addPerson():
        This function is used when I pressed addPerson button and it open a window where I can add a
        person if it is not yet registered.Then it will show a QMessageBox where it tells me if it was 
        or wasn't added with succes.
    def showMeetTime():
        This function is activated if I pressed the showMeetTime button and it will open a window that
        has the role to show me a meeteing that is between two dates.Of course it will give a message
        if the two dates are not valid
    def showAllMeets():
        This function is activated when I pressed the showAllMeets button and it will show me all 
        programmed meetings.
    def searchMeetHost():
        This function is activated when I pressed the searchMeetHost and it will show me all meets 
        where I am the host.
    def exportMeets():
        This function is activated when I pressed the exportMeets button and it will export all my 
        meetings where I am the host or I am invited in an calendar format --> .ics file. 
    def importMeets():
        This function is activated when I pressed the importMeets button and it will imports all
        meets from an .ics file from where I can chose the path and it will verify id those meets
        or invitations exists or not.I it exists it will give a message that tell us that those
        meets or invites already exists.
    def addMeet():
        This function is activated when I press addMeet button and it has the role to open
        a window from where I can chose all invited participants and then if those persons
        exists it will say in a QMesageBox that the meet was added with succes else it 
        will say that those persons does not exists. 
    def searchPersons():
        This function is activated When I press searchPersons and it will open a window from
        where after 2 strings(firstname,lastname) it will search users with those 
        caracteristics in order.
    def addPersonToMeet():
        This function is activated whe I press addPersonToMeet button and it will open a window
        from where I can add a person to a specific meeting.It will tell me in a QMessageBox if
        that person is not in my database,my meeting exists or person added succesfully.
    def deletePersonMeet():
        This function has the role to delete an invited person from a meet and it is activated
        when I press the deletePersonMeet.If that person does not exists it will give a QMessageBox
        where it say that it doesn't exists.
    def deleteMeet():
        This function is activated when I press the deleteMeet button and it has the role to
        delete a meet if I am the host of it,but firstly it deletes the invited persons from it.
        If that meet doesn't exists or I am not the host it will show a QMessageBox with this 
        information or in other case that the meet was succesfully deleted.
    def searchInvitation():
        This function is activated when I press the searchInvitation and it will show all invitations
        with that username.If the username does not exists it will show a specify message
    def accountSettings():
        This function has the role to open an window with the propriety that I can delete my account
        or I can update my firstname or lastname.
    """

    def __init__(self,username):
        """
        Constructs all the necessary attributes for the login window object.

        Parameters
        ----------
        username : str
        It represents the username of the user that is logged in the application.
        """
        super().__init__()
        self.username = username      
        self.initUI()
        self.addPersonWindow = None
        self.showAllMeetsWindow = None
        self.addPersonToMeetWindow = None
        self.addMeetWindow = None
        self.showMeetTimeWindow = None
        self.exports = None
        self.hostMeet = None
        self.searchPersWindow = None
        self.deletePersonWindowMeet = None
        self.deleteAmeetWindow = None
        self.searchInvitationsWindow = None

    def initUI(self):
        """
        Constructs all the necessary attributes for my control panel window interface.
        Eleven buttons with a specify functionality.

        Parameters
        ----------
        """

        self.setWindowTitle('Control Panel')
        self.setGeometry(300, 300, 600, 600)
        gridLayout = QGridLayout()
        self.setLayout(gridLayout)

        userLabel = QLabel(f'Nume: {self.username}', self)
        dateLabel = QLabel(f'Dată: {datetime.now().strftime("%Y-%m-%d")}', self)
        timeLabel = QLabel(f'Oră: {datetime.now().strftime("%H:%M:%S")}', self)

        gridLayout.addWidget(userLabel, 4, 0)
        gridLayout.addWidget(dateLabel, 5, 0)
        gridLayout.addWidget(timeLabel, 6, 0)

        buttonLabels = [
            "AddPerson", "ShowMeetTime", "ShowAllMeets","SearchMeetHost",
            "ExportMeets", "ImportMeets", "AddMeet","SearchPersons",
            "AddPersonToMeet", "DeletePersonMeet", "DeleteMeet","SearchInvitation"
        ]

        buttonWidth = 150
        buttonHeight = 150

        for i, label in enumerate(buttonLabels):
            button = QPushButton(label, self)
            button.setFixedSize(buttonWidth, buttonHeight)
            button.clicked.connect(lambda checked, b=button: self.onButtonClicked(b))
            row = i // 4
            col = i % 4
            gridLayout.addWidget(button, row, col)

        lowerButtonHeight = 50
        lowerButtonWidth = 150
        lowerButtonLabel = ["AccountSettings"]
                
        for i, label in enumerate(lowerButtonLabel):
            button = QPushButton(label, self)
            button.setFixedSize(lowerButtonWidth, lowerButtonHeight)
            button.clicked.connect(lambda checked, b=button: self.onButtonClicked(b))
            row = i // 3 + 3
            col = i % 3 + 2
            gridLayout.addWidget(button, row, col)
        
        gridLayout.setRowStretch(0, 1)
        gridLayout.setRowStretch(4, 1)
        gridLayout.setColumnStretch(0, 1)
        gridLayout.setColumnStretch(4, 1)

    def onButtonClicked(self, button):
        """
        This function is activate when we click a button and the it verify what type of
        button is it,then after that it will execute a function for a specify functionality.

        Parameters
        ----------
        button : QPushButton
        It represents a button from my control panel window.
        """

        button_text = button.text()
        if button_text == "AddPerson":
            self.addPerson()
        elif button_text == "ShowMeetTime":
            self.showMeetTime()
        elif button_text == "ShowAllMeets":
            self.showAllMeets()
        elif button_text == "SearchMeetHost":
            self.searchMeetHost()
        elif button_text == "ExportMeets":
            self.exportMeets()
        elif button_text == "ImportMeets":
            self.importMeets()
        elif button_text == "AddMeet":
            self.addMeet()
        elif button_text == "SearchPersons":
            self.searchPersons()
        elif button_text == "AddPersonToMeet":
            self.addPersonToMeet()
        elif button_text == "DeletePersonMeet":
            self.deletePersonMeet()
        elif button_text == "DeleteMeet":
            self.deleteMeet()
        elif button_text == "SearchInvitation":
            self.searchInvitation()
        elif button_text == "AccountSettings":
            self.accountSettings()
    
    def addPerson(self):
        """
        This function is activate when we click a button and the it verify what type of
        button is it,then after that it will execute a function for a specify functionality.

        Parameters
        ----------
        button : QPushButton
        It represents a button from my control panel window.
        """

        self.addPersonWindow = person.AddPersonWindow()
        self.addPersonWindow.show()
        return
    
    def showMeetTime(self):
        """
        This function will open a window with 2 texts for hours and 2 
        texts for dates,then it will show all meets from those interval.
        It verify if those data are corecly and will give a message if they're not. 

        Parameters
        ----------
        """

        self.showMeetTimeWindow = showMeetTimes.MeetTimes()
        self.showMeetTimeWindow.show()
        return
    
    def showAllMeets(self):
        """
        This function has the role to open an window and show in it all meetings from
        my database.

        Parameters
        ----------
        """

        self.idMeets = allMeetsId.MeetAfterId(self.username)
        self.idMeets.selectTimes()
        return
    
    def searchMeetHost(self):
        """
        This function will show a window where there are all meets where the 
        logged user is host.

        Parameters
        ----------
        """

        self.showAllMeetsWindow = hostMeets.MeetHostAfterId(self.username)
        self.showAllMeetsWindow.selectTimes()
        return 
    
    def exportMeets(self):
        """
        This function has the role to export data like invites or meetings in a calendary
        format .ics .

        Parameters
        ----------
        """

        self.exports = exports.ExportCalendar(self.username)
        self.exports.Export()
        return
    
    def importMeets(self):
        """
        This function has the role to import data from a file with calendary format
        .ics into my data base.Firstly it will open a window from where I can chose my 
        filepath and the it will import invites or meets.

        Parameters
        ----------
        """

        self.imports = imports.ImportCalendar(self.username)
        self.imports.OpenFile()
        self.imports.Import()
        return
    
    def addMeet(self):
        """
        This function has the role to open a window and there it will add a 
        new meet with any user that I insert in textbox if it exists.If
        users does not exists it will show a failure message.The username
        is used for being the host of this meet.

        Parameters
        ----------
        """

        self.addMeetWindow = addNewMeet.addMeetings(self.username)
        self.addMeetWindow.show()
        return
    
    def searchPersons(self): #de vazut
        """
        This function has the role to open a window from where I can search a person
        afler some characters in his firstname and lastname and the those will be showed
        in a new window.

        Parameters
        ----------
        """

        self.searchPersWindow = searchPers.SearchPersons()
        self.searchPersWindow.show()
        return 
    
    def addPersonToMeet(self):
        """
        This function is used for adding a person to a meet and if that person username
        inserted in my window exists it will create an invitation for it where the meet
        must be one where I am the host.It will show succes if that condition is respected
        or failure if it isn't.

        Parameters
        ----------
        """

        self.addPersonToMeetWindow = addPersToMeet.addPersonToMeet(self.username)
        self.addPersonToMeetWindow.show()

    def deletePersonMeet(self):
        """
        This function has the role to delete a person from a meeting by eliminating it's
        invitation if that one exists and it's username exists and the meeting exists too.
        It will show failure if these operation couldn't be executed or succes if it could be.

        Parameters
        ----------
        """

        self.deletePersonWindowMeet = deletePersonFromMeet.DeletePersonWindow(self.username)
        self.deletePersonWindowMeet.show()
        return
    
    def deleteMeet(self):
        """
        This function has the role to delete a meeting where the logged person is the
        host id but before it will verify if the meet exists and it will delete all
        invitations for that meet.

        Parameters
        ----------
        """

        self.deleteAmeetWindow = deletMeets.DeleteMeet(self.username)
        self.deleteAmeetWindow.show()
        return
    
    def searchInvitation(self): #
        """
        This function has the role to search invitations after a username and
        those invitations will be showed in a window.

        Parameters
        ----------
        """

        self.searchInvitationsWindow = searchInvWindow.SearchInvitations()
        self.searchInvitationsWindow.show()
        return

    def accountSettings(self): #
        """
        This function has the role to open a window from where
        I have the option to update my name,lastname or I can delete
        my account. 

        Parameters
        ----------
        """

        self.addPerson = person.AddPersonWindow()
        self.addPerson.show()
        return                                   