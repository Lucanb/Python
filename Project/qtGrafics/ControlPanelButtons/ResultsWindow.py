from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea, QApplication
from datetime import datetime, timedelta
class ResultsWindow(QWidget):
    """
    A class that represents a result window and it is used for
    displaying results of differents tipes of selects in our database.

    ...

    Atributes
    ---------
    results : str
        A string that represents our results after using an management class for
        selecting the necessary results from our database.
    Methods
    -------
    def initUI():
        This function is responsabile for creating the window specifications
        and displaying the results and a scrollbar.
    """
    def __init__(self, results):
        """
        Constructs all the necessary attributes for the result window object.

        Parameters
        ----------
        results : str
            I use this string with selected items from my database to display 
            informations given by select comands.
        """
        
        super().__init__()
        self.results = results
        self.initUI()

    def initUI(self):
        """
        Constructs all the necessary attributes for displaying a window
        with my results obtainded be a select comand and a scrollbar.

        Parameters
        ----------
        """

        self.setWindowTitle('Meetings')
        self.setGeometry(200, 200, 500, 400)

        layout = QVBoxLayout()

        myScorllBar = QScrollArea(self)
        myScorllBar.setWidgetResizable(True)

        content = QWidget()
        contentLayout = QVBoxLayout(content)

        for result in self.results:
            num_elements = len(result)
            parseResult = []
            for element in result:
                if isinstance(element, datetime):
                    formatted_datetime = element.strftime("%H:%M:%S%z")
                    parseResult.append(formatted_datetime)
                else:
                    parseResult.append(str(element))
            print(parseResult)
            label = QLabel(str(parseResult), content)
            contentLayout.addWidget(label)

        content.setLayout(contentLayout)
        myScorllBar.setWidget(content)
        layout.addWidget(myScorllBar)

        self.setLayout(layout)