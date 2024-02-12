import qtGrafics.logIn as qt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton,QHBoxLayout, QVBoxLayout,QMessageBox

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyApplication = qt.LogIn()
    MyApplication.show()
    sys.exit(app.exec_())