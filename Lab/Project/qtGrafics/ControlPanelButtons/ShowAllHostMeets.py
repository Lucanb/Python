import sys
import db.handler.meetings_maagement as managementMeet
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox,QScrollArea
import ControlPanelButtons.ResultsWindow as resW
import db.handler.personsManagement as person

class MeetHostAfterId(QWidget):
    """
    A class that represents a window which shows us all meetings(ones where we were invited or we are hosts).
    This window will appear when we press the button ShowAllMeets from control panel and it will have all
    meetings from my database.
    ...

    Atributes
    ---------
    username : str
        It represents our username and it is used too se what are the meets
    that we are hosts in our database
    resultsWindow : class
        It is initialised with none but it will represent a window class where all
        meets will be showed.
    Methods
    -------
    def selectTimes():
        Represents a function that creates our window object and activates it and that
        using a person and a meting manager it will save select results and then put them
        in my window.
    """

    def __init__(self,username):
        """
        Constructs all the necessary attributes for selecting necesay data and then 
        displaying it in a new window class.

        Parameters
        ----------
        username : str
            Is used for verifing the meets where I am the host.
        """
        super().__init__()
        self.resultsWindow = None
        self.username = username

    def selectTimes(self):
        """
        A function that use meetings management class and person management class
        for accesing the necesary data from my database and then creating a new
        window class that will be added to curent class argument and that will
        show my results.

        Parameters
        ----------
        """
        
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
