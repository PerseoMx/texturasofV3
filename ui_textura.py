# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'textura.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 835)
        MainWindow.setStyleSheet(u"background-color: #dce4e7;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #f4f7f8;")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"		background-color: rgb(41, 41, 41);\n"
"		color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	text-align:left;\n"
"	height:30px;\n"
"	border:none;\n"
"	padding-left:10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:#FFFFFF;\n"
"	color:#292929;\n"
"	font-wight:bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(40, 40))
        self.label_3.setMaximumSize(QSize(40, 40))
        self.label_3.setPixmap(QPixmap(u":/images/logo1.svg"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.btn_Calcular02 = QPushButton(self.icon_name_widget)
        self.btn_Calcular02.setObjectName(u"btn_Calcular02")
        icon = QIcon()
        icon.addFile(u":/images/calcular2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/images/calcular1.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_Calcular02.setIcon(icon)
        self.btn_Calcular02.setIconSize(QSize(25, 25))
        self.btn_Calcular02.setCheckable(True)
        self.btn_Calcular02.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_Calcular02)

        self.btn_Triangulo02 = QPushButton(self.icon_name_widget)
        self.btn_Triangulo02.setObjectName(u"btn_Triangulo02")
        icon1 = QIcon()
        icon1.addFile(u":/images/Triangulo2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/images/Triangulo1.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_Triangulo02.setIcon(icon1)
        self.btn_Triangulo02.setIconSize(QSize(25, 25))
        self.btn_Triangulo02.setCheckable(True)
        self.btn_Triangulo02.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_Triangulo02)

        self.btn_Metodo02 = QPushButton(self.icon_name_widget)
        self.btn_Metodo02.setObjectName(u"btn_Metodo02")
        icon2 = QIcon()
        icon2.addFile(u":/images/metodologia2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/images/metodologia1.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_Metodo02.setIcon(icon2)
        self.btn_Metodo02.setIconSize(QSize(25, 25))
        self.btn_Metodo02.setCheckable(True)
        self.btn_Metodo02.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_Metodo02)

        self.btn_pH02 = QPushButton(self.icon_name_widget)
        self.btn_pH02.setObjectName(u"btn_pH02")
        icon3 = QIcon()
        icon3.addFile(u":/images/pH2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/images/pH1.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_pH02.setIcon(icon3)
        self.btn_pH02.setIconSize(QSize(25, 25))
        self.btn_pH02.setCheckable(True)
        self.btn_pH02.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_pH02)

        self.btn_Soporte02 = QPushButton(self.icon_name_widget)
        self.btn_Soporte02.setObjectName(u"btn_Soporte02")
        icon4 = QIcon()
        icon4.addFile(u":/images/soprte2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/images/soprte1.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_Soporte02.setIcon(icon4)
        self.btn_Soporte02.setIconSize(QSize(25, 25))
        self.btn_Soporte02.setCheckable(True)
        self.btn_Soporte02.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_Soporte02)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 248, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.btn_salir02 = QPushButton(self.icon_name_widget)
        self.btn_salir02.setObjectName(u"btn_salir02")
        icon5 = QIcon()
        icon5.addFile(u":/images/Logout2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/images/Logout1.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_salir02.setIcon(icon5)
        self.btn_salir02.setIconSize(QSize(25, 25))
        self.btn_salir02.setCheckable(True)
        self.btn_salir02.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.btn_salir02)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(41, 41, 41);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	height:30px;\n"
"	border:none;\n"
"	border-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:#FFFFFF;\n"
"	\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 9, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/images/logo1.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.btn_Calcular01 = QPushButton(self.icon_only_widget)
        self.btn_Calcular01.setObjectName(u"btn_Calcular01")
        self.btn_Calcular01.setIcon(icon)
        self.btn_Calcular01.setIconSize(QSize(25, 25))
        self.btn_Calcular01.setCheckable(True)
        self.btn_Calcular01.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_Calcular01)

        self.btn_Triangulo01 = QPushButton(self.icon_only_widget)
        self.btn_Triangulo01.setObjectName(u"btn_Triangulo01")
        self.btn_Triangulo01.setIcon(icon1)
        self.btn_Triangulo01.setIconSize(QSize(25, 25))
        self.btn_Triangulo01.setCheckable(True)
        self.btn_Triangulo01.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_Triangulo01)

        self.btn_Metodo01 = QPushButton(self.icon_only_widget)
        self.btn_Metodo01.setObjectName(u"btn_Metodo01")
        self.btn_Metodo01.setIcon(icon2)
        self.btn_Metodo01.setIconSize(QSize(25, 25))
        self.btn_Metodo01.setCheckable(True)
        self.btn_Metodo01.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_Metodo01)

        self.btn_pH01 = QPushButton(self.icon_only_widget)
        self.btn_pH01.setObjectName(u"btn_pH01")
        self.btn_pH01.setIcon(icon3)
        self.btn_pH01.setIconSize(QSize(25, 25))
        self.btn_pH01.setCheckable(True)
        self.btn_pH01.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_pH01)

        self.btn_Soporte01 = QPushButton(self.icon_only_widget)
        self.btn_Soporte01.setObjectName(u"btn_Soporte01")
        self.btn_Soporte01.setIcon(icon4)
        self.btn_Soporte01.setIconSize(QSize(25, 25))
        self.btn_Soporte01.setCheckable(True)
        self.btn_Soporte01.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_Soporte01)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 248, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_salir01 = QPushButton(self.icon_only_widget)
        self.btn_salir01.setObjectName(u"btn_salir01")
        self.btn_salir01.setIcon(icon5)
        self.btn_salir01.setIconSize(QSize(25, 25))
        self.btn_salir01.setCheckable(True)
        self.btn_salir01.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_salir01)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_widget = QWidget(self.main_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(0, 45))
        self.layoutWidget = QWidget(self.header_widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 10, 971, 35))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_menu = QPushButton(self.layoutWidget)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setStyleSheet(u"border:none;")
        icon6 = QIcon()
        icon6.addFile(u":/images/Menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu.setIcon(icon6)
        self.btn_menu.setIconSize(QSize(30, 30))
        self.btn_menu.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_menu)

        self.horizontalSpacer = QSpacerItem(148, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.txt_buscar = QLineEdit(self.layoutWidget)
        self.txt_buscar.setObjectName(u"txt_buscar")
        self.txt_buscar.setMinimumSize(QSize(300, 0))
        self.txt_buscar.setMaximumSize(QSize(300, 33))
        self.txt_buscar.setStyleSheet(u"	background-color: rgb(255, 255, 255);\n"
"	height:31px;	\n"
"	border: 1px solid gray;\n"
"	border-color: #a4ddd4;\n"
"	border-radius: 4px;\n"
"	color: black;")

        self.horizontalLayout.addWidget(self.txt_buscar)

        self.btn_buscar = QPushButton(self.layoutWidget)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setMinimumSize(QSize(100, 30))
        self.btn_buscar.setMaximumSize(QSize(130, 30))
        self.btn_buscar.setStyleSheet(u"background-color: rgb(114, 207, 192);\n"
"color: black;\n"
"font-wight:bold;\n"
"border-radius: 8px;")
        self.btn_buscar.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_buscar)

        self.horizontalSpacer_2 = QSpacerItem(238, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_calculator = QPushButton(self.layoutWidget)
        self.btn_calculator.setObjectName(u"btn_calculator")
        self.btn_calculator.setStyleSheet(u"border:none;")
        icon7 = QIcon()
        icon7.addFile(u":/images/calculator.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_calculator.setIcon(icon7)
        self.btn_calculator.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_calculator)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: #f4f7f8;")
        self.Calcular_page = QWidget()
        self.Calcular_page.setObjectName(u"Calcular_page")
        self.frame = QFrame(self.Calcular_page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 90, 551, 321))
        self.frame.setStyleSheet(u"QFrame{\n"
"	\n"
"	border-radius:8px;\n"
"	border: 1px solid gray;\n"
"	border-color: #a4ddd4;\n"
"	background-color: rgb(255, 255, 255);\n"
"	color:black;\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel{\n"
"	border:none;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 531, 301))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.layoutWidget1)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(114, 207, 192);\n"
"	color:black;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	height:25px;	\n"
"	border:none;\n"
"	border-radius:4px;\n"
"	\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:#292929;\n"
"	font-wight:bold;\n"
"	color:white;\n"
"	border-radius: 8px;\n"
"	\n"
"}")
        self.layoutWidget2 = QWidget(self.widget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 20, 233, 261))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.layoutWidget2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setBold(True)
        self.label_18.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_18)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lb_Arena_cm = QLabel(self.layoutWidget2)
        self.lb_Arena_cm.setObjectName(u"lb_Arena_cm")

        self.verticalLayout_9.addWidget(self.lb_Arena_cm)

        self.lb_Arcilla_cm = QLabel(self.layoutWidget2)
        self.lb_Arcilla_cm.setObjectName(u"lb_Arcilla_cm")

        self.verticalLayout_9.addWidget(self.lb_Arcilla_cm)

        self.lb_Limo_cm = QLabel(self.layoutWidget2)
        self.lb_Limo_cm.setObjectName(u"lb_Limo_cm")

        self.verticalLayout_9.addWidget(self.lb_Limo_cm)

        self.lb_Total_cm = QLabel(self.layoutWidget2)
        self.lb_Total_cm.setObjectName(u"lb_Total_cm")

        self.verticalLayout_9.addWidget(self.lb_Total_cm)


        self.horizontalLayout_7.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.txt_Arena = QLineEdit(self.layoutWidget2)
        self.txt_Arena.setObjectName(u"txt_Arena")
        self.txt_Arena.setMaximumSize(QSize(16777215, 33))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.txt_Arena.setFont(font2)
        self.txt_Arena.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.txt_Arena.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_8.addWidget(self.txt_Arena)

        self.txt_Arcilla = QLineEdit(self.layoutWidget2)
        self.txt_Arcilla.setObjectName(u"txt_Arcilla")
        self.txt_Arcilla.setMaximumSize(QSize(16777215, 33))
        self.txt_Arcilla.setFont(font2)
        self.txt_Arcilla.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_8.addWidget(self.txt_Arcilla)

        self.txt_Limo = QLineEdit(self.layoutWidget2)
        self.txt_Limo.setObjectName(u"txt_Limo")
        self.txt_Limo.setMaximumSize(QSize(16777215, 33))
        self.txt_Limo.setFont(font2)
        self.txt_Limo.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_8.addWidget(self.txt_Limo)

        self.txt_TotalCm = QLineEdit(self.layoutWidget2)
        self.txt_TotalCm.setObjectName(u"txt_TotalCm")
        self.txt_TotalCm.setMaximumSize(QSize(16777215, 33))
        self.txt_TotalCm.setFont(font2)
        self.txt_TotalCm.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_8.addWidget(self.txt_TotalCm)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)


        self.verticalLayout_13.addLayout(self.horizontalLayout_7)

        self.btn_calcular_por = QPushButton(self.layoutWidget2)
        self.btn_calcular_por.setObjectName(u"btn_calcular_por")
        self.btn_calcular_por.setMaximumSize(QSize(16777215, 31))
        self.btn_calcular_por.setCheckable(True)

        self.verticalLayout_13.addWidget(self.btn_calcular_por)


        self.horizontalLayout_10.addWidget(self.widget)

        self.widget_2 = QWidget(self.layoutWidget1)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(114, 207, 192);\n"
"	color:black;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	height:25px;	\n"
"	border:none;\n"
"	border-radius: 4px;\n"
"	\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:#292929;\n"
"	font-wight:bold;\n"
"	color:white;\n"
"	border-radius:8px;\n"
"	\n"
"}")
        self.layoutWidget3 = QWidget(self.widget_2)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 20, 226, 261))
        self.verticalLayout_14 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.layoutWidget3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 20))
        self.label_19.setFont(font1)

        self.verticalLayout_14.addWidget(self.label_19)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_12 = QLabel(self.layoutWidget3)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_7.addWidget(self.label_12)

        self.label_13 = QLabel(self.layoutWidget3)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_7.addWidget(self.label_13)

        self.label_14 = QLabel(self.layoutWidget3)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_7.addWidget(self.label_14)

        self.label_15 = QLabel(self.layoutWidget3)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_7.addWidget(self.label_15)


        self.horizontalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.txt_ArenaPor = QLineEdit(self.layoutWidget3)
        self.txt_ArenaPor.setObjectName(u"txt_ArenaPor")
        self.txt_ArenaPor.setMaximumSize(QSize(16777215, 33))
        self.txt_ArenaPor.setFont(font2)
        self.txt_ArenaPor.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.txt_ArenaPor)

        self.txt_ArcillaPor = QLineEdit(self.layoutWidget3)
        self.txt_ArcillaPor.setObjectName(u"txt_ArcillaPor")
        self.txt_ArcillaPor.setMaximumSize(QSize(16777215, 33))
        self.txt_ArcillaPor.setFont(font2)
        self.txt_ArcillaPor.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.txt_ArcillaPor)

        self.txt_LimoPor = QLineEdit(self.layoutWidget3)
        self.txt_LimoPor.setObjectName(u"txt_LimoPor")
        self.txt_LimoPor.setMaximumSize(QSize(16777215, 33))
        self.txt_LimoPor.setFont(font2)
        self.txt_LimoPor.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.txt_LimoPor)

        self.txt_Total = QLineEdit(self.layoutWidget3)
        self.txt_Total.setObjectName(u"txt_Total")
        self.txt_Total.setMaximumSize(QSize(16777215, 33))
        self.txt_Total.setFont(font2)
        self.txt_Total.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.txt_Total)


        self.horizontalLayout_8.addLayout(self.verticalLayout_6)


        self.verticalLayout_14.addLayout(self.horizontalLayout_8)

        self.btn_calcular_textu = QPushButton(self.layoutWidget3)
        self.btn_calcular_textu.setObjectName(u"btn_calcular_textu")
        self.btn_calcular_textu.setMaximumSize(QSize(16777215, 31))
        self.btn_calcular_textu.setCheckable(True)

        self.verticalLayout_14.addWidget(self.btn_calcular_textu)


        self.horizontalLayout_10.addWidget(self.widget_2)

        self.frame_2 = QFrame(self.Calcular_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 420, 981, 341))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	\n"
"	border-radius:8px;\n"
"	border: 1px solid gray;\n"
"	border-color: #a4ddd4;\n"
"	background-color: rgb(255, 255, 255);\n"
"	color:black;\n"
"}\n"
"\n"
"QLabel{\n"
"	border:none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.table_datos = QTableWidget(self.frame_2)
        if (self.table_datos.columnCount() < 8):
            self.table_datos.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_datos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_datos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_datos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_datos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_datos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_datos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_datos.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_datos.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.table_datos.setObjectName(u"table_datos")
        self.table_datos.setGeometry(QRect(10, 10, 961, 321))
        self.table_datos.setMaximumSize(QSize(961, 16777215))
        self.table_datos.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	background-color:#67c6b7;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #ffffff;\n"
"	background-color: #ffffff;\n"
"}")
        self.table_datos.verticalHeader().setMinimumSectionSize(22)
        self.frame_3 = QFrame(self.Calcular_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(570, 90, 421, 321))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	\n"
"	border-radius:8px;\n"
"	border: 1px solid gray;\n"
"	border-color: #a4ddd4;\n"
"	background-color: rgb(255, 255, 255);\n"
"	color:black;\n"
"}\n"
"\n"
"QLabel{\n"
"	\n"
"	background-color: #caf0ec;\n"
"	\n"
"	border:none;\n"
"	\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:#292929;\n"
"	font-wight:bold;\n"
"	color:white;\n"
"	border-radius: 8px;\n"
"	\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget4 = QWidget(self.frame_3)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(12, 22, 381, 291))
        self.verticalLayout_15 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.layoutWidget4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(355, 40))
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_15.addWidget(self.label_17)

        self.lab_textura = QLabel(self.layoutWidget4)
        self.lab_textura.setObjectName(u"lab_textura")
        self.lab_textura.setMinimumSize(QSize(0, 60))
        self.lab_textura.setMaximumSize(QSize(400, 300))
        font3 = QFont()
        font3.setPointSize(25)
        font3.setBold(True)
        self.lab_textura.setFont(font3)
        self.lab_textura.setStyleSheet(u"border-radius:10px;")
        self.lab_textura.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lab_textura.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.lab_textura)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_guardar = QPushButton(self.layoutWidget4)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setMaximumSize(QSize(130, 31))
        self.btn_guardar.setStyleSheet(u"background-color: rgb(114, 207, 192);\n"
"color: black;")
        self.btn_guardar.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.btn_guardar)

        self.btn_actualizar = QPushButton(self.layoutWidget4)
        self.btn_actualizar.setObjectName(u"btn_actualizar")
        self.btn_actualizar.setMaximumSize(QSize(130, 31))
        self.btn_actualizar.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.btn_actualizar)


        self.verticalLayout_15.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_eliminar = QPushButton(self.layoutWidget4)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setMaximumSize(QSize(130, 31))
        self.btn_eliminar.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn_eliminar.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.btn_eliminar)

        self.btn_limpiar = QPushButton(self.layoutWidget4)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setMaximumSize(QSize(130, 31))
        self.btn_limpiar.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.btn_limpiar)


        self.verticalLayout_15.addLayout(self.horizontalLayout_11)

        self.frame_4 = QFrame(self.Calcular_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 0, 981, 80))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	border-radius:8px;\n"
"	border: 1px solid gray;\n"
"	border-color: #a4ddd4;\n"
"	color:black;\n"
"\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	height:31px;	\n"
"	border: 1px solid gray;\n"
"	border-color: #a4ddd4;\n"
"	border-radius: 4px;\n"
"	color: black;\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	height:31px;	\n"
"	border: 1px solid gray;\n"
"	border-color: #a4ddd4;\n"
"	border-radius: 4px;\n"
"	color: black;\n"
"	\n"
"}\n"
"\n"
"QLabel{\n"
"	border:none;\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget5 = QWidget(self.frame_4)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(46, 11, 901, 62))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lb_nombre = QLabel(self.layoutWidget5)
        self.lb_nombre.setObjectName(u"lb_nombre")

        self.verticalLayout_12.addWidget(self.lb_nombre)

        self.txt_nombre = QLineEdit(self.layoutWidget5)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setMaximumSize(QSize(300, 33))

        self.verticalLayout_12.addWidget(self.txt_nombre)


        self.horizontalLayout_6.addLayout(self.verticalLayout_12)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lb_lote = QLabel(self.layoutWidget5)
        self.lb_lote.setObjectName(u"lb_lote")

        self.verticalLayout_11.addWidget(self.lb_lote)

        self.txt_lote = QLineEdit(self.layoutWidget5)
        self.txt_lote.setObjectName(u"txt_lote")
        self.txt_lote.setMaximumSize(QSize(300, 33))

        self.verticalLayout_11.addWidget(self.txt_lote)


        self.horizontalLayout_6.addLayout(self.verticalLayout_11)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lb_fecha = QLabel(self.layoutWidget5)
        self.lb_fecha.setObjectName(u"lb_fecha")

        self.verticalLayout_10.addWidget(self.lb_fecha)

        self.date_fecha = QDateEdit(self.layoutWidget5)
        self.date_fecha.setObjectName(u"date_fecha")
        self.date_fecha.setMaximumSize(QSize(300, 33))
        self.date_fecha.setCalendarPopup(True)
        self.date_fecha.setDate(QDate(2026, 9, 16))

        self.verticalLayout_10.addWidget(self.date_fecha)


        self.horizontalLayout_6.addLayout(self.verticalLayout_10)

        self.stackedWidget.addWidget(self.Calcular_page)
        self.Triangulo_page = QWidget()
        self.Triangulo_page.setObjectName(u"Triangulo_page")
        self.frame_5 = QFrame(self.Triangulo_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 20, 1011, 731))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.widget1 = QWidget(self.frame_5)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(50, 10, 941, 681))
        self.verticalLayout_16 = QVBoxLayout(self.widget1)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget1)
        self.label_10.setObjectName(u"label_10")
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color: black;")

        self.verticalLayout_16.addWidget(self.label_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(128, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label_7 = QLabel(self.widget1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(601, 581))
        self.label_7.setFont(font4)
        self.label_7.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.label_7.setStyleSheet(u"border-image: url(:/images/TrianguloTextura.png);")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.horizontalSpacer_4 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_16.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.Triangulo_page)
        self.Metodo_page = QWidget()
        self.Metodo_page.setObjectName(u"Metodo_page")
        self.frame_6 = QFrame(self.Metodo_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 10, 971, 751))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 60, 511, 631))
        font5 = QFont()
        font5.setPointSize(11)
        self.label_4.setFont(font5)
        self.label_4.setWordWrap(True)
        self.widget2 = QWidget(self.frame_6)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(640, 50, 311, 681))
        self.verticalLayout_17 = QVBoxLayout(self.widget2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.widget2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 20, 151, 141))
        self.label_5.setStyleSheet(u"border-image: url(:/images/botellaA.png);")

        self.verticalLayout_17.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.widget2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 30, 131, 141))
        self.label_8.setStyleSheet(u"border-image: url(:/images/botellaB.png);")

        self.verticalLayout_17.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.widget2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 20, 171, 171))
        self.label_9.setStyleSheet(u"border-image: url(:/images/botellaC.png);")

        self.verticalLayout_17.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.Metodo_page)
        self.pH_page = QWidget()
        self.pH_page.setObjectName(u"pH_page")
        self.lb_pH = QLabel(self.pH_page)
        self.lb_pH.setObjectName(u"lb_pH")
        self.lb_pH.setGeometry(QRect(260, 150, 501, 91))
        font6 = QFont()
        font6.setPointSize(50)
        font6.setBold(True)
        self.lb_pH.setFont(font6)
        self.lb_pH.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lb_pH.setLineWidth(1)
        self.horizontalSlider = QSlider(self.pH_page)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(250, 270, 511, 71))
        self.horizontalSlider.setSizeIncrement(QSize(0, 0))
        self.horizontalSlider.setBaseSize(QSize(0, 0))
        font7 = QFont()
        font7.setPointSize(9)
        self.horizontalSlider.setFont(font7)
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(14)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setPageStep(10)
        self.horizontalSlider.setValue(7)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.horizontalSlider.setTickInterval(1)
        self.lb_pH_Resultado = QLabel(self.pH_page)
        self.lb_pH_Resultado.setObjectName(u"lb_pH_Resultado")
        self.lb_pH_Resultado.setGeometry(QRect(260, 470, 501, 81))
        font8 = QFont()
        font8.setPointSize(30)
        font8.setBold(True)
        self.lb_pH_Resultado.setFont(font8)
        self.lb_pH_Resultado.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.layoutWidget6 = QWidget(self.pH_page)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(250, 350, 511, 71))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lb_ph0 = QLabel(self.layoutWidget6)
        self.lb_ph0.setObjectName(u"lb_ph0")
        self.lb_ph0.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.horizontalLayout_5.addWidget(self.lb_ph0)

        self.lb_ph01 = QLabel(self.layoutWidget6)
        self.lb_ph01.setObjectName(u"lb_ph01")
        self.lb_ph01.setStyleSheet(u"background-color: rgb(244, 106, 7);")

        self.horizontalLayout_5.addWidget(self.lb_ph01)

        self.lb_ph02 = QLabel(self.layoutWidget6)
        self.lb_ph02.setObjectName(u"lb_ph02")
        self.lb_ph02.setStyleSheet(u"background-color: rgb(251, 199, 1);")

        self.horizontalLayout_5.addWidget(self.lb_ph02)

        self.lb_ph03 = QLabel(self.layoutWidget6)
        self.lb_ph03.setObjectName(u"lb_ph03")
        self.lb_ph03.setStyleSheet(u"background-color: rgb(244, 239, 0);")

        self.horizontalLayout_5.addWidget(self.lb_ph03)

        self.lb_ph04 = QLabel(self.layoutWidget6)
        self.lb_ph04.setObjectName(u"lb_ph04")
        self.lb_ph04.setStyleSheet(u"background-color: rgb(180, 213, 0);")

        self.horizontalLayout_5.addWidget(self.lb_ph04)

        self.lb_ph05 = QLabel(self.layoutWidget6)
        self.lb_ph05.setObjectName(u"lb_ph05")
        self.lb_ph05.setStyleSheet(u"background-color: rgb(130, 194, 45);")

        self.horizontalLayout_5.addWidget(self.lb_ph05)

        self.lb_ph06 = QLabel(self.layoutWidget6)
        self.lb_ph06.setObjectName(u"lb_ph06")
        self.lb_ph06.setStyleSheet(u"background-color: rgb(74, 184, 61);")

        self.horizontalLayout_5.addWidget(self.lb_ph06)

        self.lb_ph07 = QLabel(self.layoutWidget6)
        self.lb_ph07.setObjectName(u"lb_ph07")
        self.lb_ph07.setStyleSheet(u"background-color: rgb(6, 169, 63);")

        self.horizontalLayout_5.addWidget(self.lb_ph07)

        self.lb_ph08 = QLabel(self.layoutWidget6)
        self.lb_ph08.setObjectName(u"lb_ph08")
        self.lb_ph08.setStyleSheet(u"background-color: rgb(26, 182, 101);")

        self.horizontalLayout_5.addWidget(self.lb_ph08)

        self.lb_ph09 = QLabel(self.layoutWidget6)
        self.lb_ph09.setObjectName(u"lb_ph09")
        self.lb_ph09.setStyleSheet(u"background-color: rgb(0, 186, 181);")

        self.horizontalLayout_5.addWidget(self.lb_ph09)

        self.lb_ph10 = QLabel(self.layoutWidget6)
        self.lb_ph10.setObjectName(u"lb_ph10")
        self.lb_ph10.setStyleSheet(u"background-color: rgb(65, 143, 205);")

        self.horizontalLayout_5.addWidget(self.lb_ph10)

        self.lb_ph11 = QLabel(self.layoutWidget6)
        self.lb_ph11.setObjectName(u"lb_ph11")
        self.lb_ph11.setStyleSheet(u"background-color: rgb(55, 81, 168);")

        self.horizontalLayout_5.addWidget(self.lb_ph11)

        self.lb_ph12 = QLabel(self.layoutWidget6)
        self.lb_ph12.setObjectName(u"lb_ph12")
        self.lb_ph12.setStyleSheet(u"background-color: rgb(90, 80, 166);")

        self.horizontalLayout_5.addWidget(self.lb_ph12)

        self.lb_ph13 = QLabel(self.layoutWidget6)
        self.lb_ph13.setObjectName(u"lb_ph13")
        self.lb_ph13.setStyleSheet(u"background-color: rgb(97, 68, 160);")

        self.horizontalLayout_5.addWidget(self.lb_ph13)

        self.lb_ph14 = QLabel(self.layoutWidget6)
        self.lb_ph14.setObjectName(u"lb_ph14")
        self.lb_ph14.setStyleSheet(u"background-color: rgb(70, 41, 134);")

        self.horizontalLayout_5.addWidget(self.lb_ph14)

        self.stackedWidget.addWidget(self.pH_page)
        self.Soporte_page = QWidget()
        self.Soporte_page.setObjectName(u"Soporte_page")
        self.label_6 = QLabel(self.Soporte_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 90, 471, 471))
        font9 = QFont()
        font9.setPointSize(10)
        font9.setBold(False)
        self.label_6.setFont(font9)
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_6.setWordWrap(True)
        self.stackedWidget.addWidget(self.Soporte_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.txt_nombre, self.txt_lote)
        QWidget.setTabOrder(self.txt_lote, self.date_fecha)
        QWidget.setTabOrder(self.date_fecha, self.txt_Arena)
        QWidget.setTabOrder(self.txt_Arena, self.txt_Arcilla)
        QWidget.setTabOrder(self.txt_Arcilla, self.txt_Limo)
        QWidget.setTabOrder(self.txt_Limo, self.txt_TotalCm)
        QWidget.setTabOrder(self.txt_TotalCm, self.btn_calcular_por)
        QWidget.setTabOrder(self.btn_calcular_por, self.txt_ArenaPor)
        QWidget.setTabOrder(self.txt_ArenaPor, self.txt_ArcillaPor)
        QWidget.setTabOrder(self.txt_ArcillaPor, self.txt_LimoPor)
        QWidget.setTabOrder(self.txt_LimoPor, self.txt_Total)
        QWidget.setTabOrder(self.txt_Total, self.btn_calcular_textu)
        QWidget.setTabOrder(self.btn_calcular_textu, self.btn_guardar)
        QWidget.setTabOrder(self.btn_guardar, self.btn_actualizar)
        QWidget.setTabOrder(self.btn_actualizar, self.table_datos)
        QWidget.setTabOrder(self.table_datos, self.btn_menu)
        QWidget.setTabOrder(self.btn_menu, self.btn_Calcular01)
        QWidget.setTabOrder(self.btn_Calcular01, self.btn_Triangulo01)
        QWidget.setTabOrder(self.btn_Triangulo01, self.btn_Metodo01)
        QWidget.setTabOrder(self.btn_Metodo01, self.btn_pH01)
        QWidget.setTabOrder(self.btn_pH01, self.btn_Soporte01)
        QWidget.setTabOrder(self.btn_Soporte01, self.btn_salir01)
        QWidget.setTabOrder(self.btn_salir01, self.btn_Calcular02)
        QWidget.setTabOrder(self.btn_Calcular02, self.btn_Triangulo02)
        QWidget.setTabOrder(self.btn_Triangulo02, self.btn_Metodo02)
        QWidget.setTabOrder(self.btn_Metodo02, self.btn_pH02)
        QWidget.setTabOrder(self.btn_pH02, self.btn_Soporte02)
        QWidget.setTabOrder(self.btn_Soporte02, self.btn_salir02)
        QWidget.setTabOrder(self.btn_salir02, self.btn_calculator)
        QWidget.setTabOrder(self.btn_calculator, self.label_7)
        QWidget.setTabOrder(self.label_7, self.horizontalSlider)

        self.retranslateUi(MainWindow)
        self.btn_menu.toggled.connect(self.icon_only_widget.setHidden)
        self.btn_menu.toggled.connect(self.icon_name_widget.setVisible)
        self.btn_Soporte01.toggled.connect(self.btn_Soporte02.setChecked)
        self.btn_pH01.toggled.connect(self.btn_pH02.setChecked)
        self.btn_Metodo01.toggled.connect(self.btn_Metodo02.setChecked)
        self.btn_Triangulo01.toggled.connect(self.btn_Triangulo02.setChecked)
        self.btn_Calcular01.toggled.connect(self.btn_Calcular02.setChecked)
        self.btn_Calcular02.toggled.connect(self.btn_Calcular01.setChecked)
        self.btn_Triangulo02.toggled.connect(self.btn_Triangulo01.setChecked)
        self.btn_Metodo02.toggled.connect(self.btn_Metodo01.setChecked)
        self.btn_pH02.toggled.connect(self.btn_pH01.setChecked)
        self.btn_Soporte02.toggled.connect(self.btn_Soporte01.setChecked)
        self.btn_salir01.toggled.connect(MainWindow.close)
        self.btn_salir02.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextureSoft", None))
        self.btn_Calcular02.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.btn_Triangulo02.setText(QCoreApplication.translate("MainWindow", u"Tri\u00e1ngulo", None))
        self.btn_Metodo02.setText(QCoreApplication.translate("MainWindow", u"Metodolog\u00eda", None))
        self.btn_pH02.setText(QCoreApplication.translate("MainWindow", u"pH", None))
        self.btn_Soporte02.setText(QCoreApplication.translate("MainWindow", u"Soporte", None))
        self.btn_salir02.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.label.setText("")
        self.btn_Calcular01.setText("")
        self.btn_Triangulo01.setText("")
        self.btn_Metodo01.setText("")
        self.btn_pH01.setText("")
        self.btn_Soporte01.setText("")
        self.btn_salir01.setText("")
        self.btn_menu.setText("")
        self.txt_buscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar datos...", None))
        self.btn_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btn_calculator.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Part\u00edculas precipitadas (cm)", None))
        self.lb_Arena_cm.setText(QCoreApplication.translate("MainWindow", u"Arena (cm)", None))
        self.lb_Arcilla_cm.setText(QCoreApplication.translate("MainWindow", u"Arcilla (cm)", None))
        self.lb_Limo_cm.setText(QCoreApplication.translate("MainWindow", u"Limo (cm)", None))
        self.lb_Total_cm.setText(QCoreApplication.translate("MainWindow", u"Total (cm)", None))
        self.txt_Arena.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txt_Arcilla.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txt_Limo.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_calcular_por.setText(QCoreApplication.translate("MainWindow", u"Calcular %", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Proporci\u00f3n de part\u00edculas (%)", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Arena (%)", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Arcilla (%)", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Limo (%)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Total (%)", None))
        self.txt_ArenaPor.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txt_ArcillaPor.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txt_LimoPor.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_calcular_textu.setText(QCoreApplication.translate("MainWindow", u"Determinar Textura", None))
        ___qtablewidgetitem = self.table_datos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        ___qtablewidgetitem1 = self.table_datos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        ___qtablewidgetitem2 = self.table_datos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        ___qtablewidgetitem3 = self.table_datos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Lote/parcela", None))
        ___qtablewidgetitem4 = self.table_datos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Arena (%)", None))
        ___qtablewidgetitem5 = self.table_datos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Arcilla (%)", None))
        ___qtablewidgetitem6 = self.table_datos.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Limo (%)", None))
        ___qtablewidgetitem7 = self.table_datos.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Textura Clasificada", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"DIAGN\u00d3STICO TEXTURAL", None))
        self.lab_textura.setText("")
        self.btn_guardar.setText(QCoreApplication.translate("MainWindow", u"Guardar en la BD", None))
        self.btn_actualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar datos", None))
        self.btn_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar datos", None))
        self.btn_limpiar.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.lb_nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre y Apellido (T\u00e9cnico / Analista)", None))
        self.lb_lote.setText(QCoreApplication.translate("MainWindow", u"Lote / Parcela", None))
        self.lb_fecha.setText(QCoreApplication.translate("MainWindow", u"Fecha de Muestreo", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Tri\u00e1ngulo de textura de suelos", None))
        self.label_7.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">TEXTURA DEL SUELO </span><span style=\" color:#000000;\"><br/>La textura indica el contenido relativo de part\u00edculas de diferente tama\u00f1o, como la arena, el limo y la arcilla, en el suelo. Para conocer la textura del suelo en campo, se presentan varias metodolog\u00edas, la presente aplicaci\u00f3n considera la metodolog\u00eda de precipitaci\u00f3n de part\u00edculas, siendo muy pr\u00e1ctica y con resultados confiables.</span></p><p align=\"justify\"><span style=\" font-weight:600; color:#000000;\">PRUEBA DE LA BOTELLA PARA DETERMINAR LA TEXTURA DEL SUELO</span></p><p align=\"justify\"><span style=\" color:#000000;\">- En una botella de vidrio colocar 8 cm de suelo previamente mezclada, y ll\u00e9nela con agua</span></p><p align=\"justify\"><span style=\" color:#000000;\">- Agitar bien y dejar reposar durante una hora, durante ese tiempo las part\u00edculas de m\u00e1s peso se han sedimentado.</span></p><p align=\"justify\"><span "
                        "style=\" color:#000000;\">- En la capa inferior se deposita la arena, en la parte media el limo y en la superior la arcilla. Si el agua no est\u00e1 completamente transparente, se debe a que la parte de arcilla mas fina aun est\u00e1 mezclada con el agua.</span></p><p align=\"justify\"><span style=\" color:#000000;\">- En la superficie del agua pueden flotar fragmentos de materia org\u00e1nica.</span></p><p align=\"justify\"><span style=\" color:#000000;\">- Medir la profundidad de la arena, limo y la arcilla en cent\u00edmetros, los datos en cent\u00edmetros introducir en el programa TextSoft en los campos respectivos,  para calcular las proporciones en porcentaje</span></p></body></html>", None))
        self.label_5.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"l", None))
        self.label_9.setText("")
        self.lb_pH.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">pH</p></body></html>", None))
        self.lb_pH_Resultado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.lb_ph0.setText("")
        self.lb_ph01.setText("")
        self.lb_ph02.setText("")
        self.lb_ph03.setText("")
        self.lb_ph04.setText("")
        self.lb_ph05.setText("")
        self.lb_ph06.setText("")
        self.lb_ph07.setText("")
        self.lb_ph08.setText("")
        self.lb_ph09.setText("")
        self.lb_ph10.setText("")
        self.lb_ph11.setText("")
        self.lb_ph12.setText("")
        self.lb_ph13.setText("")
        self.lb_ph14.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Acerca de TextureSoft</span></p><p align=\"justify\">TextureSoft en su versi\u00f3n 3.0, es una aplicaci\u00f3n desarrollada en lenguaje Python 3.5, con una interfaz gr\u00e1fica creada en Pyside6-designer.</p><p align=\"justify\">La aplicaci\u00f3n permite determinar la textura del suelo, basado en la clasificaci\u00f3n de USDA, considerando 12 Clases texturales (ver tri\u00e1ngulo textural).</p><p align=\"justify\">La versi\u00f3n 3.0 integra una base de datos en SQlite, donde almacena de datos, puede actualizar y eliminar datos, con una interfaz moderna.</p><p align=\"justify\">Versi\u00f3n suministrada por Ecoproductivo 2022-2026</p><p align=\"justify\"><a href=\"https://ecoproductivo.com/\"><span style=\" font-weight:700; text-decoration: underline; color:#308cc6;\">https://ecoproductivo.com</span></a></p><p align=\"justify\">Version: 3.0(x86_64)</p><p align=\"justify\">Elaborado por: Ing. Richard Estrada<br/></p></body"
                        "></html>", None))
    # retranslateUi

