#!/usr/bin/env python3
# coding=utf-8

import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView

answers = ['', '', '']  # 1 - form2, 2 - form3, 3 - form4


class Form1(QtWidgets.QMainWindow):
    # аргумент str говорит о том, что сигнал должен быть сторокового типа
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form1, self).__init__()
        uic.loadUi('uis/form1.ui', self)

        self.setWindowTitle('Приветствие')

        self.btn_exit.clicked.connect(self.close)
        self.btn_begin.clicked.connect(self.next)

    def next(self):
        self.switch_window.emit('1>2')


class Form2(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form2, self).__init__()
        uic.loadUi('uis/form2.ui', self)

        self.setWindowTitle('Детство')

        # устанавливаем картинку label_img
        self.label_img.setPixmap(QPixmap('images/books.jpeg'))
        # подгоняем картинку под размер label_img
        self.label_img.setScaledContents(True)

        # если ранее ответ был уже выбран, то показываем его заново
        answers[0] = self.listWidget.currentItem().text()
        self.label_selected.setText('Выбрано: ' + answers[0])

        self.listWidget.itemClicked.connect(self.item_click)

        self.btn_back.clicked.connect(self.back)
        self.btn_next.clicked.connect(self.next)

    def item_click(self, item):
        answers[0] = item.text()
        self.label_selected.setText('Выбрано: ' + answers[0])

    def back(self):
        self.switch_window.emit('1<2')

    def next(self):
        self.switch_window.emit('2>3')


class Form3(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form3, self).__init__()
        uic.loadUi('uis/form3.ui', self)

        self.setWindowTitle('Отрочество')

        self.label_img.setPixmap(QPixmap('images/sport.jpeg'))
        self.label_img.setScaledContents(True)

        answers[1] = self.comboBox.currentText()
        self.label_selected.setText('Выбрано: ' + answers[1])

        self.comboBox.activated.connect(self.handleActivated)

        self.btn_back.clicked.connect(self.back)
        self.btn_next.clicked.connect(self.next)

    def handleActivated(self, index):
        answers[1] = self.comboBox.itemText(index)
        self.label_selected.setText('Выбрано: ' + answers[1])

    def back(self):
        self.switch_window.emit('2<3')

    def next(self):
        self.switch_window.emit('3>4')


class Form4(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form4, self).__init__()
        uic.loadUi('uis/form4.ui', self)

        self.setWindowTitle('Юность')

        self.label_img.setPixmap(QPixmap('images/profession.jpeg'))
        self.label_img.setScaledContents(True)

        if self.radioButton_1.isChecked():
            answers[2] = self.radioButton_1.text()
        if self.radioButton_2.isChecked():
            answers[2] = self.radioButton_2.text()
        if self.radioButton_3.isChecked():
            answers[2] = self.radioButton_3.text()
        if self.radioButton_4.isChecked():
            answers[2] = self.radioButton_4.text()
        if self.radioButton_5.isChecked():
            answers[2] = self.radioButton_5.text()
        if self.radioButton_6.isChecked():
            answers[2] = self.radioButton_6.text()

        self.label_selected.setText('Выбрано: ' + answers[2])

        # ставим события на radioButtons
        self.radioButton_1.toggled.connect(
            lambda: self.onToggled(self.radioButton_1))
        self.radioButton_2.toggled.connect(
            lambda: self.onToggled(self.radioButton_2))
        self.radioButton_3.toggled.connect(
            lambda: self.onToggled(self.radioButton_3))
        self.radioButton_4.toggled.connect(
            lambda: self.onToggled(self.radioButton_4))
        self.radioButton_5.toggled.connect(
            lambda: self.onToggled(self.radioButton_5))
        self.radioButton_6.toggled.connect(
            lambda: self.onToggled(self.radioButton_6))

        self.btn_back.clicked.connect(self.back)
        self.btn_next.clicked.connect(self.next)

    def onToggled(self, radiobutton):
        if radiobutton.isChecked():
            answers[2] = radiobutton.text()
            self.label_selected.setText('Выбрано: ' + answers[2])

    def back(self):
        self.switch_window.emit('3<4')

    def next(self):
        self.switch_window.emit('4>5')


class Form5(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form5, self).__init__()
        uic.loadUi('uis/form5.ui', self)

        self.setWindowTitle('Результат')

        # запрещаем редактирование таблицы
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # присваиваем значение ячейкам таблицы
        self.tableWidget.setItem(0, 0,
                                 QTableWidgetItem('Во сколько лет вы научились читать?'))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(answers[0]))

        self.tableWidget.setItem(1, 0,
                                 QTableWidgetItem('Ходили ли куда-то помимо школы?'))
        self.tableWidget.setItem(1, 1, QTableWidgetItem(answers[1]))

        self.tableWidget.setItem(2, 0,
                                 QTableWidgetItem('Почему вы выбрали свою специальность?'))
        self.tableWidget.setItem(2, 1, QTableWidgetItem(answers[2]))

        self.btn_back.clicked.connect(self.back)
        self.btn_exit.clicked.connect(self.close)

    def back(self):
        self.switch_window.emit("4<5")


'''
Класс управления переключения окон
'''


class Controller:
    def __init__(self):
        pass

    def select_forms(self, text):
        if text == '1':
            self.form1 = Form1()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()

        if text == '1>2':
            self.form2 = Form2()
            self.form2.switch_window.connect(self.select_forms)
            self.form2.show()
            self.form1.close()

        if text == '2>3':
            self.form3 = Form3()
            self.form3.switch_window.connect(self.select_forms)
            self.form3.show()
            self.form2.close()

        if text == '3>4':
            self.form4 = Form4()
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
            self.form3.close()

        if text == '4>5':
            self.form5 = Form5()
            self.form5.switch_window.connect(self.select_forms)
            self.form5.show()
            self.form4.close()

        if text == '4<5':
            self.form4 = Form4()
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
            self.form5.close()

        if text == '3<4':
            self.form3 = Form3()
            self.form3.switch_window.connect(self.select_forms)
            self.form3.show()
            self.form4.close()

        if text == '2<3':
            self.form2 = Form2()
            self.form2.switch_window.connect(self.select_forms)
            self.form2.show()
            self.form3.close()

        if text == '1<2':
            self.form1 = Form1()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()
            self.form2.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.select_forms("1")
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
