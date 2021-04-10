import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import pathlib
import json

r = requests.get('http://api.weatherstack.com/current?access_key=e682fc6afa695092cdeb579da6354f04&units=f&query=Los Angeles, California')
pathlib.Path('data.json').write_bytes(r.content)


