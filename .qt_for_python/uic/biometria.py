# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Felipe\Desktop\APS Processamento de Imagem e Visão Computacional\biometria.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_autentication(object):
    def setupUi(self, autentication):
        autentication.setObjectName("autentication")
        autentication.resize(443, 531)
        autentication.setStyleSheet("font: 12pt \"Poppins\";")
        self.centralwidget = QtWidgets.QWidget(autentication)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 380, 391, 23))
        self.progressBar.setProperty("value", 1)
        self.progressBar.setObjectName("progressBar")
        self.text_progressbar = QtWidgets.QLabel(self.centralwidget)
        self.text_progressbar.setGeometry(QtCore.QRect(30, 330, 381, 51))
        self.text_progressbar.setStyleSheet("font: 8.5pt \"Poppins\";")
        self.text_progressbar.setAlignment(QtCore.Qt.AlignCenter)
        self.text_progressbar.setObjectName("text_progressbar")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(120, 20, 211, 301))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("c:\\Users\\Felipe\\Desktop\\APS Processamento de Imagem e Visão Computacional\\biometria.png"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 410, 241, 28))
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"background-color: rgb(131, 198, 131);\n"
"color: white;\n"
"border-radius: 10px;\n"
"padding:5px;\n"
"font-size:18px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"    \n"
"    background-color: rgb(105, 198, 127);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 401, 271))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        autentication.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(autentication)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 443, 42))
        self.menubar.setObjectName("menubar")
        autentication.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(autentication)
        self.statusbar.setObjectName("statusbar")
        autentication.setStatusBar(self.statusbar)

        self.retranslateUi(autentication)
        QtCore.QMetaObject.connectSlotsByName(autentication)

    def retranslateUi(self, autentication):
        _translate = QtCore.QCoreApplication.translate
        autentication.setWindowTitle(_translate("autentication", "Autentication"))
        self.text_progressbar.setText(_translate("autentication", "Autenticando Biometria"))
        self.pushButton.setText(_translate("autentication", "Processar Autenticação"))
