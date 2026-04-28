import sys
import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QVBoxLayout, QWidget, QLineEdit, \
    QGridLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")

        centralW = QWidget()
        self.setCentralWidget(centralW)

        mainLayout = QVBoxLayout(centralW)

        # Preview and Output Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setFocusPolicy(Qt.NoFocus)
        self.display.setAlignment(Qt.AlignRight)
        mainLayout.addWidget(self.display)

        # Grid
        grid = QGridLayout()
        mainLayout.addLayout(grid)

        # Buttons
        self.b0 = QPushButton("0")
        self.b1 = QPushButton("1")
        self.b2 = QPushButton("2")
        self.b3 = QPushButton("3")
        self.b4 = QPushButton("4")
        self.b5 = QPushButton("5")
        self.b6 = QPushButton("6")
        self.b7 = QPushButton("7")
        self.b8 = QPushButton("8")
        self.b9 = QPushButton("9")

        self.btimes = QPushButton("*")
        self.bdivided = QPushButton("/")
        self.bplus = QPushButton("+")
        self.bminus = QPushButton("-")

        self.bequal = QPushButton("=")
        self.bdot = QPushButton(".")
        self.bc = QPushButton("C")
        self.bb = QPushButton("<-")

        self.blb = QPushButton("(")
        self.brb = QPushButton(")")

        # adding the buttons to the grid
        grid.addWidget(self.bb, 0 , 0)
        grid.addWidget(self.blb, 0, 1)
        grid.addWidget(self.brb, 0, 2)
        grid.addWidget(self.bc, 0, 3)

        grid.addWidget(self.b7, 1, 0)
        grid.addWidget(self.b8, 1, 1)
        grid.addWidget(self.b9, 1, 2)
        grid.addWidget(self.bdivided, 1, 3)

        grid.addWidget(self.b4, 2, 0)
        grid.addWidget(self.b5, 2, 1)
        grid.addWidget(self.b6, 2, 2)
        grid.addWidget(self.btimes, 2, 3)

        grid.addWidget(self.b1, 3, 0)
        grid.addWidget(self.b2, 3, 1)
        grid.addWidget(self.b3, 3, 2)
        grid.addWidget(self.bminus, 3, 3)

        grid.addWidget(self.b0, 4, 0)
        grid.addWidget(self.bdot, 4, 1)
        grid.addWidget(self.bequal, 4, 2)
        grid.addWidget(self.bplus, 4, 3)

        # ------------------------ Logic ------------------------ #

        # Initialize calculator variables
        self.calculation = ""
        self.output = ""

        # function assignment
        self.b0.clicked.connect(lambda: self.add_symbol("0"))
        self.b1.clicked.connect(lambda: self.add_symbol("1"))
        self.b2.clicked.connect(lambda: self.add_symbol("2"))
        self.b3.clicked.connect(lambda: self.add_symbol("3"))
        self.b4.clicked.connect(lambda: self.add_symbol("4"))
        self.b5.clicked.connect(lambda: self.add_symbol("5"))
        self.b6.clicked.connect(lambda: self.add_symbol("6"))
        self.b7.clicked.connect(lambda: self.add_symbol("7"))
        self.b8.clicked.connect(lambda: self.add_symbol("8"))
        self.b9.clicked.connect(lambda: self.add_symbol("9"))

        self.bplus.clicked.connect(lambda: self.add_symbol("+"))
        self.bminus.clicked.connect(lambda: self.add_symbol("-"))
        self.btimes.clicked.connect(lambda: self.add_symbol("*"))
        self.bdivided.clicked.connect(lambda: self.add_symbol("/"))

        self.blb.clicked.connect(lambda: self.add_symbol("("))
        self.brb.clicked.connect(lambda: self.add_symbol(")"))

        self.bequal.clicked.connect(self.calculate)
        self.bdot.clicked.connect(lambda: self.add_symbol("."))
        self.bc.clicked.connect(self.clear)
        self.bb.clicked.connect(self.backspace)

    def add_symbol(self, symbol):
        self.calculation += symbol
        self.display.setText(self.calculation)

    allowed = set("0123456789+-*/(). ")

    def calculate(self):
        if not all(c in allowed for c in self.calculation):
            self.display.setText("Error: Ungültige Zeichen")
            return

        try:
            result = eval(self.calculation)
        except Exception as e:
            self.display.setText(f"Error: {e}")
            return

        self.display.setText(f"{self.calculation} = {result}")

    def clear (self):
        self.calculation = ""
        self.display.setText("")

    def backspace(self):
        self.calculation = self.calculation[:-1]
        self.display.setText(self.calculation)


app = QApplication(sys.argv)

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)
qss_path = os.path.join(base_path, "style.qss")

with open(qss_path, "r") as f:
    app.setStyleSheet(f.read())
window = MainWindow()
window.show()

app.exec()