import sqlite3
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog
from random import randint
from addwidget import Ui_Form

import sqlite3


class AddRow(QWidget, Ui_Form):
    def __init__(self, mainapp):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.addrow)
        self.con = sqlite3.connect('coffee.sqlite')
        self.mainapp = mainapp

    def addrow(self):
        name = self.lineEdit.text().strip()
        amount = self.lineEdit_2.text().strip()
        isGood = self.lineEdit_3.text().strip()
        cur = self.con.cursor()
        try:
            amount = int(amount)
            if isGood not in ['FALSE', 'TRUE']:
                raise Exception
            cur.execute("""INSERT INTO coffee(name, pckgs_amount, istasty) VALUES(?, ?, ?)""", (name, amount, isGood))
            self.con.commit()
            self.mainapp.initTable()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddRow(None)
    ex.show()
    sys.exit(app.exec())
