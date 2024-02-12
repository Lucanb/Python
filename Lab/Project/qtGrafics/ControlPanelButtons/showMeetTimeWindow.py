import sys
import db.handler.meetings_maagement as managementMeet
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox,QScrollArea
import ControlPanelButtons.ResultsWindow as resW

class MeetTimes(QWidget):
    """
    A class that represents a window which shows 4 QLineEdit elements for construct
    my date and time.We have a QPushButton that willa ctivate a function wich
    will select the meetings that are between thos 2 date and then put them in
    a new window.
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
    def initUI(self):
        Represents a function that will create our window class with 4 QLineEdit
        elements for construct my date and time.We have a QPushButton that 
        willa ctivate a function wich will select the meetings that are between
        thos 2 date and then put them in a new window.
        
    def selectTimes():
        Represents a function that creates our window object and activates it and that
        using a person and a meting manager it will save select results and then put them
        in my window.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for selecting necesay data and then 
        displaying it in a new window class.

        Parameters
        ----------
        """

        super().__init__()
        self.resultsWindow = None
        self.initUI()
    
    def initUI(self):
        """
        A function that creates my window with 4 QLineEdit buttons
        for dates and hours when meets starts and ends. It will have
        another QPushButton that will activare selectTimes function
        which will select my meetings and display them in a new window.
        
        Parameters
        ----------
        """
                
        self.setWindowTitle('Meet Times')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.beginDate = QLineEdit(self)
        self.beginDate.setPlaceholderText('Data de început (YYYY-MM-DD)')
        layout.addWidget(self.beginDate)

        self.beginTime = QLineEdit(self)
        self.beginTime.setPlaceholderText('Ora de început (HH:MM)')
        layout.addWidget(self.beginTime)

        self.endDate = QLineEdit(self)
        self.endDate.setPlaceholderText('Data de sfârșit (YYYY-MM-DD)')
        layout.addWidget(self.endDate)

        self.endTime = QLineEdit(self)
        self.endTime.setPlaceholderText('Ora de sfârșit (HH:MM)')
        layout.addWidget(self.endTime)

        self.validButton = QPushButton('OK', self)
        self.validButton.clicked.connect(self.selectTimes)
        layout.addWidget(self.validButton)

        self.setLayout(layout)

    def selectTimes(self):
        """
        A function that use meetings management class for accesing
        the necesary data from my database and then creating a new
        window class that will be added to curent class argument 
        and that will show my results.

        Parameters
        ----------
        """

        startDate = self.beginDate.text()
        startTime = self.beginTime.text()
        endDate = self.endDate.text()
        endTime = self.endTime.text()

        hour_begin = f"{startDate} {startTime}:00+02"
        hour_end = f"{endDate} {endTime}:00+02"

        meets = managementMeet.MeetingManagement()
        try:
            results = meets.selectMeetsByTime(hour_begin,hour_end)
            print(results)
            if self.resultsWindow is not None:
                self.resultsWindow.close()
            self.resultsWindow = resW.ResultsWindow(results)
            self.resultsWindow.show()
        except Exception as error_selectingDb:
            QMessageBox.warning(self, 'Error', str(error_selectingDb))
