from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea, QApplication
class ResultsWindow(QWidget):
    def __init__(self, results):
        super().__init__()
        self.results = results
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Meetings')
        self.setGeometry(200, 200, 500, 400)

        layout = QVBoxLayout()

        myScorllBar = QScrollArea(self)
        myScorllBar.setWidgetResizable(True)

        content = QWidget()
        contentLayout = QVBoxLayout(content)

        for result in self.results:
            label = QLabel(str(result), content)
            contentLayout.addWidget(label)

        content.setLayout(contentLayout)
        myScorllBar.setWidget(content)
        layout.addWidget(myScorllBar)

        self.setLayout(layout)