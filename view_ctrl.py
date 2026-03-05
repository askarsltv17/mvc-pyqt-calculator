from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
from model import Calculator 

class CalculatorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.calculator = Calculator() 
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MVC Calculator')
        self.setFixedSize(300, 400)
        layout = QVBoxLayout()

       
        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        layout.addWidget(self.display)

        
        grid = QGridLayout()
        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            '0': (3, 0), 'C': (3, 1), '=': (3, 2), '+': (3, 3),
        }

        for text, pos in buttons.items():
            btn = QPushButton(text)
            btn.setFixedSize(60, 60)
            btn.clicked.connect(lambda _, t=text: self.handle_click(t))
            grid.addWidget(btn, *pos)

        layout.addLayout(grid)
        self.setLayout(layout)

    def handle_click(self, char):
        if char == '=':
            res = self.calculator.calculate()
            self.display.setText(str(res))
        elif char == 'C':
            self.calculator.clear_expression()
            self.display.setText("")
        else:
            self.calculator.add_to_expression(char)
            self.display.setText(self.calculator.get_expression())