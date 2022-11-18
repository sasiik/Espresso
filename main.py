import sqlite3
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog
from random import randint
from widget import Ui_Form

import sqlite3


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initTable()

    def initTable(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        self.tableWidget.setModel(model)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
