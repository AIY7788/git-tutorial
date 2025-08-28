
import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first gui")
        self.setGeometry(550 , 200 , 800 , 800)
        self.setWindowIcon(QIcon("20250409_bing.jpg"))

        label = QLabel("Hello Guy", self)
        label.setFont(QFont("Arial",30))
        label.setGeometry(0 , 0 , 800 , 200)
        label.setStyleSheet("color : #222C2D;"
                            "background-color : #3C45B5;"
                            "font-weight : bold;"
                            "text-decoration : underline;")

        #label.setAlignment(Qt.AlignTop)
        #label.setAlignment(Qt.AlignBottom)
        #label.setAlignment(Qt.AlignRight)
        label.setAlignment(Qt.AlignCenter)
        #label.setAlignment(Qt.AlignLeft)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 