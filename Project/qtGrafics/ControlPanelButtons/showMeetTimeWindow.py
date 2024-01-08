import sys
import db.handler.meetings_maagement as managementMeet
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox,QScrollArea
import ControlPanelButtons.ResultsWindow as resW

class MeetTimes(QWidget):
    def __init__(self):
        super().__init__()
        self.resultsWindow = None
        self.initUI()
    
    def initUI(self):
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
        startDate = self.beginDate.text()
        startTime = self.beginTime.text()
        endDate = self.endDate.text()
        endTime = self.endTime.text()

        hour_begin = f"{startDate} {startTime}:00+03"
        hour_end = f"{endDate} {endTime}:00+03"

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
