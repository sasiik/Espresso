import sqlite3
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog
from random import randint
from widget import Ui_Form
from add import AddRow
import sqlite3


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initTable()
        self.pushButton.clicked.connect(self.addTask)

    def initTable(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        self.tableView.setModel(model)
        db.close()

    def addTask(self):
        self.addTaskWindow = AddRow(self)
        self.addTaskWindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
