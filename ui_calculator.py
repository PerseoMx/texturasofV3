# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(300, 450)
        widget.setStyleSheet(u"background-color: black;")
        self.main_label = QLabel(widget)
        self.main_label.setObjectName(u"main_label")
        self.main_label.setGeometry(QRect(10, 70, 281, 81))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(35)
        self.main_label.setFont(font)
        self.main_label.setStyleSheet(u"color:white;")
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.main_label_2 = QLabel(widget)
        self.main_label_2.setObjectName(u"main_label_2")
        self.main_label_2.setGeometry(QRect(10, 20, 281, 41))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(16)
        self.main_label_2.setFont(font1)
        self.main_label_2.setStyleSheet(u"color: white;")
        self.main_label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.gridLayoutWidget = QWidget(widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 180, 281, 261))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_7 = QPushButton(self.gridLayoutWidget)
        self.btn_7.setObjectName(u"btn_7")
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(17)
        self.btn_7.setFont(font2)
        self.btn_7.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.btn_7, 0, 0, 1, 1)

        self.btn_0 = QPushButton(self.gridLayoutWidget)
        self.btn_0.setObjectName(u"btn_0")
        self.btn_0.setFont(font2)
        self.btn_0.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.btn_0, 3, 0, 1, 2)

        self.btn_decimal = QPushButton(self.gridLayoutWidget)
        self.btn_decimal.setObjectName(u"btn_decimal")
        self.btn_decimal.setFont(font2)
        self.btn_decimal.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.btn_decimal, 3, 2, 1, 1)

        self.btn_8 = QPushButton(self.gridLayoutWidget)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setFont(font2)
        self.btn_8.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.btn_8, 0, 1, 1, 1)

        self.btn_4 = QPushButton(self.gridLayoutWidget)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setFont(font2)
        self.btn_4.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)

        self.btn_igual = QPushButton(self.gridLayoutWidget)
        self.btn_igual.setObjectName(u"btn_igual")
        self.btn_igual.setFont(font2)
        self.btn_igual.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.btn_igual, 4, 2, 1, 2)

        self.btn_c = QPushButton(self.gridLayoutWidget)
        self.btn_c.setObjectName(u"btn_c")
        self.btn_c.setFont(font2)
        self.btn_c.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.btn_c, 4, 0, 1, 2)

        self.btn_minus = QPushButton(self.gridLayoutWidget)
        self.btn_minus.setObjectName(u"btn_minus")
        self.btn_minus.setFont(font2)
        self.btn_minus.setStyleSheet(u"background-color: #EEA10C;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.btn_minus, 1, 3, 1, 1)

        self.btn_6 = QPushButton(self.gridLayoutWidget)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setFont(font2)
        self.btn_6.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)

        self.btn_9 = QPushButton(self.gridLayoutWidget)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setFont(font2)
        self.btn_9.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.btn_9, 0, 2, 1, 1)

        self.btn_5 = QPushButton(self.gridLayoutWidget)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setFont(font2)
        self.btn_5.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)

        self.btn_1 = QPushButton(self.gridLayoutWidget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setFont(font2)
        self.btn_1.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.btn_1, 2, 0, 1, 1)

        self.btn_multiply = QPushButton(self.gridLayoutWidget)
        self.btn_multiply.setObjectName(u"btn_multiply")
        self.btn_multiply.setFont(font2)
        self.btn_multiply.setStyleSheet(u"background-color: #EEA10C;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.btn_multiply, 2, 3, 1, 1)

        self.btn_3 = QPushButton(self.gridLayoutWidget)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setFont(font2)
        self.btn_3.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.btn_3, 2, 2, 1, 1)

        self.btn_divide = QPushButton(self.gridLayoutWidget)
        self.btn_divide.setObjectName(u"btn_divide")
        self.btn_divide.setFont(font2)
        self.btn_divide.setStyleSheet(u"background-color: #EEA10C;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.btn_divide, 3, 3, 1, 1)

        self.btn_plus = QPushButton(self.gridLayoutWidget)
        self.btn_plus.setObjectName(u"btn_plus")
        self.btn_plus.setFont(font2)
        self.btn_plus.setStyleSheet(u"background-color: #EEA10C;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.btn_plus, 0, 3, 1, 1)

        self.btn_2 = QPushButton(self.gridLayoutWidget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setFont(font2)
        self.btn_2.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.btn_2, 2, 1, 1, 1)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Form", None))
        self.main_label.setText(QCoreApplication.translate("widget", u"0", None))
        self.main_label_2.setText(QCoreApplication.translate("widget", u"0", None))
        self.btn_7.setText(QCoreApplication.translate("widget", u"7", None))
        self.btn_0.setText(QCoreApplication.translate("widget", u"0", None))
        self.btn_decimal.setText(QCoreApplication.translate("widget", u".", None))
        self.btn_8.setText(QCoreApplication.translate("widget", u"8", None))
        self.btn_4.setText(QCoreApplication.translate("widget", u"4", None))
        self.btn_igual.setText(QCoreApplication.translate("widget", u"=", None))
        self.btn_c.setText(QCoreApplication.translate("widget", u"C", None))
        self.btn_minus.setText(QCoreApplication.translate("widget", u"-", None))
        self.btn_6.setText(QCoreApplication.translate("widget", u"6", None))
        self.btn_9.setText(QCoreApplication.translate("widget", u"9", None))
        self.btn_5.setText(QCoreApplication.translate("widget", u"5", None))
        self.btn_1.setText(QCoreApplication.translate("widget", u"1", None))
        self.btn_multiply.setText(QCoreApplication.translate("widget", u"*", None))
        self.btn_3.setText(QCoreApplication.translate("widget", u"3", None))
        self.btn_divide.setText(QCoreApplication.translate("widget", u"/", None))
        self.btn_plus.setText(QCoreApplication.translate("widget", u"+", None))
        self.btn_2.setText(QCoreApplication.translate("widget", u"2", None))
    # retranslateUi

