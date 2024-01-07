import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('3x3 Button Grid')
        self.setGeometry(300, 300, 600, 600)
        gridLayout = QGridLayout()
        self.setLayout(gridLayout)
        for i in range(9):
            button = QPushButton(f'Button {i+1}', self)
            buttonWidth = 200
            buttonHeight = 200
            button.setFixedSize(buttonWidth, buttonHeight) 
            row = i // 3
            col = i % 3
            gridLayout.addWidget(button, row, col)

        gridLayout.setRowStretch(0, 1)
        gridLayout.setRowStretch(4, 1)
        gridLayout.setColumnStretch(0, 1)
        gridLayout.setColumnStretch(4, 1)