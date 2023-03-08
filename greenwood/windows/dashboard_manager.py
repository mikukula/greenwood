from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QDialog    
from PyQt6 import uic
import sys

class DashboardManager():
    def __init__(self, dashboard):
        self.dashboard = dashboard

    def addToComboBox(self, boxName, item):
        boxName.addItem(item)
