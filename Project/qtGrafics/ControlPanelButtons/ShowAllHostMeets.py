import sys
import db.handler.meetings_maagement as managementMeet
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox,QScrollArea
import ControlPanelButtons.ResultsWindow as resW
import db.handler.personsManagement as person

class MeetHostAfterId(QWidget):
    def __init__(self,username):
        super().__init__()
        self.resultsWindow = None
        self.username = username

    def selectTimes(self):

        meets = managementMeet.MeetingManagement()
        try:
            user = person.PersonManagement()
            MyId = user.getUserId(self.username)
            print(MyId)
            results = meets.selectMeetsById(MyId)
            print(results)
            if self.resultsWindow is not None:
                self.resultsWindow.close()
            self.resultsWindow = resW.ResultsWindow(results)
            self.resultsWindow.show()
        except Exception as error_selectingDb:
            QMessageBox.warning(self, 'Error', str(error_selectingDb))
