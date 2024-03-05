# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'punto5_cilindro.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(614, 409)
        Dialog.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 40, 171, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 131, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 131, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 111, 21))
        self.label_4.setObjectName("label_4")
        self.diametro_cilindro = QtWidgets.QTextEdit(Dialog)
        self.diametro_cilindro.setGeometry(QtCore.QRect(220, 90, 101, 31))
        self.diametro_cilindro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.diametro_cilindro.setObjectName("diametro_cilindro")
        self.diametro_vastago = QtWidgets.QTextEdit(Dialog)
        self.diametro_vastago.setGeometry(QtCore.QRect(220, 140, 101, 31))
        self.diametro_vastago.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.diametro_vastago.setObjectName("diametro_vastago")
        self.presion = QtWidgets.QTextEdit(Dialog)
        self.presion.setGeometry(QtCore.QRect(220, 190, 101, 31))
        self.presion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.presion.setObjectName("presion")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 260, 111, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 310, 111, 21))
        self.label_6.setObjectName("label_6")
        self.fuerza_avance = QtWidgets.QTextEdit(Dialog)
        self.fuerza_avance.setGeometry(QtCore.QRect(220, 250, 101, 31))
        self.fuerza_avance.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fuerza_avance.setObjectName("fuerza_avance")
        self.fuerza_retroceso = QtWidgets.QTextEdit(Dialog)
        self.fuerza_retroceso.setGeometry(QtCore.QRect(220, 310, 101, 31))
        self.fuerza_retroceso.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fuerza_retroceso.setObjectName("fuerza_retroceso")
        self.boton_ejecutar = QtWidgets.QPushButton(Dialog)
        self.boton_ejecutar.setGeometry(QtCore.QRect(470, 330, 75, 23))
        self.boton_ejecutar.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.boton_ejecutar.setObjectName("boton_ejecutar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">CILINDRO DE DOBLE EFECTO</span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">diametro cilindro (cm)</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">diametro vastago (cm)</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">presion</span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">fuerza avance</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">fuerza retroceso</span></p></body></html>"))
        self.boton_ejecutar.setText(_translate("Dialog", "EXECUTE"))
    def ejecutar(self):
        diametro_cilindro = float(self.diametro_cilindro.toPlainText())
        diametro_vastago = float(self.diametro_vastago.toPlainText())
        presion_trabajo = float(self.presion.toPlainText())

        area_cilindro = np.pi * (diametro_cilindro ** 2) / 4
        area_vastago = np.pi * ((diametro_cilindro ** 2 - diametro_vastago ** 2) / 4)

        fuerza_de_avance_valor = str(area_cilindro * presion_trabajo)
        fuerza_de_retroceso_valor = str(area_vastago * presion_trabajo)
        
        self.fuerza_avance.setText(fuerza_de_avance_valor)
        self.fuerza_retroceso.setText(fuerza_de_retroceso_valor)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.boton_ejecutar.clicked.connect(ui.ejecutar)
    Dialog.show()
    sys.exit(app.exec_())