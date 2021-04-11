import sys
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)

from PyQt5.QtWinExtras import QtWin
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import requests
import pathlib
import json
import urllib

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Foreseeable")
        self.setWindowIcon(QIcon("icon.png"))
        QtWin.setCurrentProcessExplicitAppUserModelID("ModernEra.Foreseeable.1.0")
        self.setFixedWidth(700)
        self.setFixedHeight(100)
        # Create a QHBoxLayout instance
        self.layout = QHBoxLayout()
        # Add widgets to the layout
        self.lineEdit = QLineEdit()
        self.layout.addWidget(self.lineEdit)
        self.button = QPushButton("Get Temp!")
        self.button.clicked.connect(self.button_click)
        self.layout.addWidget(self.button)
        self.label = QLabel("Enter a City (and a State optionally)")
        self.layout.addWidget(self.label)
        self.image = QLabel()
        question = QPixmap('question.jpg')
        question = question.scaledToWidth(75)
        self.image.setPixmap(question)
        self.layout.addWidget(self.image)
        # Set the layout on the application's window
        self.setLayout(self.layout)
        print(self.children())

    def button_click(self):
        query = self.lineEdit.text()
        r = requests.get('http://api.weatherstack.com/current?access_key=e682fc6afa695092cdeb579da6354f04&units=f&query=' + query)
        pathlib.Path('data.json').write_bytes(r.content)

        with open('data.json') as f:
            data = json.load(f)
        self.label.setText("The current temperature in "+ query + " is " + str(data["current"]["temperature"]) + " degrees")
        imgurl = data["current"]["weather_icons"][0]
        imgdata = urllib.request.urlopen(imgurl).read()
        imagePixmap = QPixmap()
        imagePixmap.loadFromData(imgdata)
        self.image.setPixmap(imagePixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
    




