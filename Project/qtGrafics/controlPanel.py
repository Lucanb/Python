import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout,QLabel
from datetime import datetime
import ControlPanelButtons.AddPerson as person
import ControlPanelButtons.showMeetTimeWindow as showMeetTimes
import ControlPanelButtons.AllMeetsId as allMeetsId
import ControlPanelButtons.addMeets as addNewMeet
class Window(QWidget):
    def __init__(self,username):
        super().__init__()
        self.username = username      
        self.initUI()
        self.addPersonWindow = None
        self.showAllMeetsWindow = None
        self.addPersonToMeetWindow = None
        self.addMeetWindow = None
        self.showMeetTimeWindow = None

    def initUI(self):
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
        lowerButtonLabel = ["Logout","AccountSettings"]
                
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
        elif button_text == "Logout":
            self.logout()
        elif button_text == "AccountSettings":
            self.accountSettings()
    
    def addPerson(self):
        self.addPersonWindow = person.AddPersonWindow()
        self.addPersonWindow.show()
        return
    
    def showMeetTime(self):
        self.showMeetTimeWindow = showMeetTimes.MeetTimes()
        self.showMeetTimeWindow.show()
        return
    
    def showAllMeets(self):
        self.idMeets = allMeetsId.MeetAfterId(self.username)
        self.idMeets.selectTimes()
        return
    
    def searchMeetHost(self): ###
        self.showAllMeetsWindow = person.AddPersonWindow()
        self.addPerson.show()
        return 
    
    def exportMeets(self):
        self.addPerson = person.AddPersonWindow()
        self.addPerson.show()
        return
    
    def importMeets(self): ###
        self.addPerson = person.AddPersonWindow()
        self.addPerson.show()
        return
    
    def addMeet(self): #!
        self.addMeetWindow = addNewMeet.addMeetings(self.username)
        self.addMeetWindow.show()
        return
    
    def searchPersons(self):
        self.addPerson = person.AddPersonWindow()
        self.addPerson.show()
        return 
    
    def addPersonToMeet(self): #!
        self.addPerson = person.AddPersonWindow()
        self.addPerson.show()
        return
    
    def deletePersonMeet(self):
        self.addPerson = person.AddPersonWindow()
        self.addPerson.show()
        return
    
    def deleteMeet(self):
        self.addPerson = person.AddPersonWindow()
        self.addPerson.show()
        return
    
    def searchInvitation(self):
        self.addPerson = person.AddPersonWindow()
        self.addPerson.show()
        return
    
    def logout(self):
        self.addPerson = person.AddPersonWindow()
        self.addPerson.show()
        return

    def accountSettings(self):
        self.addPerson = person.AddPersonWindow()
        self.addPerson.show()
        return                                   