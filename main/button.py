
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(500, 200, 900, 800)
        self.result = 0.0
        self.initUI()

    def initUI(self):
        self.input_line = QLineEdit(self)
        self.input_line.setPlaceholderText("กรอกตัวเลขหรือ operator (เช่น +, -, *, /, exit)")

        self.output_label = QLabel("เริ่มต้นด้วยการกรอกเลข", self)

        self.btn = QPushButton("ตกลง", self)
        self.btn.clicked.connect(self.process_input)

        layout = QVBoxLayout()
        layout.addWidget(self.input_line)
        layout.addWidget(self.btn)
        layout.addWidget(self.output_label)
        self.setLayout(layout)

        self.expecting_operator = False
        self.last_operator = None

    def process_input(self):
        text = self.input_line.text().strip()
        if text == 'exit':
            self.output_label.setText("ลาก่อน!")
            self.btn.setEnabled(False)
            return

        try:
            if not self.expecting_operator:
                self.result = float(text)
                self.output_label.setText(f"เริ่มต้นที่: {self.result}")
                self.expecting_operator = True
            else:
                if text in ['+', '-', '*', '/']:
                    self.last_operator = text
                    self.output_label.setText(f"กรอกเลขต่อไป เพื่อทำ {self.last_operator}")
                    self.expecting_operator = False
                else:
                    num = float(text)
                    if self.last_operator == '+':
                        self.result += num
                    elif self.last_operator == '-':
                        self.result -= num
                    elif self.last_operator == '*':
                        self.result *= num
                    elif self.last_operator == '/':
                        if num != 0:
                            self.result /= num
                        else:
                            self.output_label.setText("หารด้วยศูนย์ไม่ได้")
                            return
                    self.output_label.setText(f"ผลลัพธ์ปัจจุบัน: {self.result}")
                    self.expecting_operator = True
        except:
            self.output_label.setText("กรุณากรอกข้อมูลให้ถูกต้อง")

        self.input_line.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())

