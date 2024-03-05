# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculadora_arrays.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from punto2_arrays import ArraysOperaciones
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox



class Ui_Dialog(object):
    
    primeraMatriz = None
    segundaMatriz = None
    filaMatriz1 = None
    columnaMatriz1 = None
    filaMatriz2 = None
    columnaMatriz2 = None
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(679, 546)
        Dialog.setStyleSheet("background-color: rgb(255, 113, 85);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 91, 31))
        self.label_2.setObjectName("label_2")
        self.numero_filas_primera_matriz = QtWidgets.QTextEdit(Dialog)
        self.numero_filas_primera_matriz.setGeometry(QtCore.QRect(160, 50, 51, 31))
        self.numero_filas_primera_matriz.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.numero_filas_primera_matriz.setObjectName("numero_filas_primera_matriz")
        self.numero_columnas_primera_matriz = QtWidgets.QTextEdit(Dialog)
        self.numero_columnas_primera_matriz.setGeometry(QtCore.QRect(160, 110, 51, 31))
        self.numero_columnas_primera_matriz.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.numero_columnas_primera_matriz.setObjectName("numero_columnas_primera_matriz")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 170, 151, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 230, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(130, 230, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(210, 230, 47, 13))
        self.label_6.setObjectName("label_6")
        self.fila_primera_matriz = QtWidgets.QTextEdit(Dialog)
        self.fila_primera_matriz.setGeometry(QtCore.QRect(50, 260, 41, 31))
        self.fila_primera_matriz.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fila_primera_matriz.setObjectName("fila_primera_matriz")
        self.columna_primera_matriz = QtWidgets.QTextEdit(Dialog)
        self.columna_primera_matriz.setGeometry(QtCore.QRect(130, 260, 41, 31))
        self.columna_primera_matriz.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.columna_primera_matriz.setObjectName("columna_primera_matriz")
        self.valor_posicion_primera_matriz = QtWidgets.QTextEdit(Dialog)
        self.valor_posicion_primera_matriz.setGeometry(QtCore.QRect(210, 260, 41, 31))
        self.valor_posicion_primera_matriz.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.valor_posicion_primera_matriz.setObjectName("valor_posicion_primera_matriz")
        self.guardar_valor_primera_matriz = QtWidgets.QPushButton(Dialog)
        self.guardar_valor_primera_matriz.setGeometry(QtCore.QRect(110, 330, 75, 23))
        self.guardar_valor_primera_matriz.setStyleSheet("background-color: rgb(102, 143, 255);")
        self.guardar_valor_primera_matriz.setObjectName("guardar_valor_primera_matriz")
        self.columna_segunda_matriz = QtWidgets.QTextEdit(Dialog)
        self.columna_segunda_matriz.setGeometry(QtCore.QRect(490, 260, 41, 31))
        self.columna_segunda_matriz.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.columna_segunda_matriz.setObjectName("columna_segunda_matriz")
        self.fila_segunda_matriz = QtWidgets.QTextEdit(Dialog)
        self.fila_segunda_matriz.setGeometry(QtCore.QRect(410, 260, 41, 31))
        self.fila_segunda_matriz.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.fila_segunda_matriz.setObjectName("fila_segunda_matriz")
        self.guardar_valor_segunda_matriz = QtWidgets.QPushButton(Dialog)
        self.guardar_valor_segunda_matriz.setGeometry(QtCore.QRect(470, 330, 75, 23))
        self.guardar_valor_segunda_matriz.setStyleSheet("background-color: rgb(102, 143, 255);")
        self.guardar_valor_segunda_matriz.setObjectName("guardar_valor_segunda_matriz")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(410, 110, 91, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(570, 230, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(450, 170, 151, 41))
        self.label_9.setObjectName("label_9")
        self.numero_filas_segunda_matriz = QtWidgets.QTextEdit(Dialog)
        self.numero_filas_segunda_matriz.setGeometry(QtCore.QRect(520, 50, 51, 31))
        self.numero_filas_segunda_matriz.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.numero_filas_segunda_matriz.setObjectName("numero_filas_segunda_matriz")
        self.numero_columnas_segunda_matriz = QtWidgets.QTextEdit(Dialog)
        self.numero_columnas_segunda_matriz.setGeometry(QtCore.QRect(520, 110, 51, 31))
        self.numero_columnas_segunda_matriz.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.numero_columnas_segunda_matriz.setObjectName("numero_columnas_segunda_matriz")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(420, 230, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(490, 230, 61, 16))
        self.label_11.setObjectName("label_11")
        self.valor_posicion_segunda_matriz = QtWidgets.QTextEdit(Dialog)
        self.valor_posicion_segunda_matriz.setGeometry(QtCore.QRect(570, 260, 41, 31))
        self.valor_posicion_segunda_matriz.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.valor_posicion_segunda_matriz.setObjectName("valor_posicion_segunda_matriz")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(410, 50, 81, 31))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(100, 10, 121, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(460, 10, 121, 21))
        self.label_14.setObjectName("label_14")
        self.operaciones = QtWidgets.QComboBox(Dialog)
        self.operaciones.setGeometry(QtCore.QRect(150, 430, 111, 31))
        self.operaciones.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.operaciones.setObjectName("operaciones")
        self.operaciones.addItem("")
        self.operaciones.addItem("")
        self.operaciones.addItem("")
        self.operaciones.addItem("")
        self.resultado = QtWidgets.QTextEdit(Dialog)
        self.resultado.setGeometry(QtCore.QRect(440, 430, 161, 31))
        self.resultado.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resultado.setObjectName("resultado")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(40, 430, 71, 31))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(340, 430, 71, 31))
        self.label_16.setObjectName("label_16")
        self.ejecutar = QtWidgets.QPushButton(Dialog)
        self.ejecutar.setGeometry(QtCore.QRect(520, 500, 75, 23))
        self.ejecutar.setStyleSheet("background-color: rgb(102, 143, 255);")
        self.ejecutar.setObjectName("ejecutar")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 150, 651, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(10, 380, 651, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(310, 160, 31, 231))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.guardar_tamano_matrices = QtWidgets.QPushButton(Dialog)
        self.guardar_tamano_matrices.setGeometry(QtCore.QRect(280, 80, 75, 23))
        self.guardar_tamano_matrices.setStyleSheet("background-color: rgb(102, 143, 255);")
        self.guardar_tamano_matrices.setObjectName("guardar_tamano_matrices")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "# DE FILAS"))
        self.label_2.setText(_translate("Dialog", "# DE COLUMNAS"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">INGRESE LOS VALORES</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "FILA"))
        self.label_5.setText(_translate("Dialog", "COLUMNA"))
        self.label_6.setText(_translate("Dialog", "VALOR"))
        self.guardar_valor_primera_matriz.setText(_translate("Dialog", "GUADAR"))
        self.guardar_valor_segunda_matriz.setText(_translate("Dialog", "GUADAR"))
        self.label_7.setText(_translate("Dialog", "# DE COLUMNAS"))
        self.label_8.setText(_translate("Dialog", "VALOR"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">INGRESE LOS VALORES</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "FILA"))
        self.label_11.setText(_translate("Dialog", "COLUMNA"))
        self.label_12.setText(_translate("Dialog", "# DE FILAS"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">PRIMERA MATRIZ</span></p></body></html>"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SEGUNDA MATRIZ</span></p></body></html>"))
        self.operaciones.setItemText(0, _translate("Dialog", "SUMA"))
        self.operaciones.setItemText(1, _translate("Dialog", "RESTA"))
        self.operaciones.setItemText(2, _translate("Dialog", "MULTIPLICACION"))
        self.operaciones.setItemText(3, _translate("Dialog", "DIVISION"))
        self.label_15.setText(_translate("Dialog", "OPERACION"))
        self.label_16.setText(_translate("Dialog", "RESULTADO"))
        self.ejecutar.setText(_translate("Dialog", "EJECUTAR"))
        self.guardar_tamano_matrices.setText(_translate("Dialog", "GUADAR"))
        
    def guardarMatriz(self):
        global  primeraMatriz
        global  segundaMatriz 
        
        global filaMatriz1 
        global columnaMatriz1 
        global filaMatriz2 
        global columnaMatriz2 
            
        arraysOperaciones = ArraysOperaciones()
            
        tamañoFila_1matriz = int(self.numero_filas_primera_matriz.toPlainText())
        tamañoColumna_1matriz = int(self.numero_columnas_primera_matriz.toPlainText())
        tamañoFila_2matriz = int(self.numero_filas_segunda_matriz.toPlainText())
        tamañoColumna_2matriz = int(self.numero_columnas_segunda_matriz.toPlainText())
        
        filaMatriz1 = tamañoFila_1matriz 
        columnaMatriz1 = tamañoColumna_1matriz
        filaMatriz2 = tamañoFila_2matriz
        columnaMatriz2 = tamañoColumna_2matriz
        
        
        primeraMatriz = ArraysOperaciones.crear_matriz(tamañoFila_1matriz,tamañoColumna_1matriz)
        segundaMatriz = ArraysOperaciones.crear_matriz(tamañoFila_2matriz,tamañoColumna_2matriz,)
        
        print(primeraMatriz)
        print(segundaMatriz)
        
        return primeraMatriz, segundaMatriz
        #guardarValor(primeraMatriz)
        
    def guardarValor1(self):
        global primeraMatriz
        
        fila = int(self.fila_primera_matriz.toPlainText())
        columna = int(self.columna_primera_matriz.toPlainText())
        valor = int(self.valor_posicion_primera_matriz.toPlainText())
        
        nuevo_valor = ArraysOperaciones.modificar_valor(primeraMatriz,fila,columna,valor)
        print(nuevo_valor)
        
    def guardarValor2(self):
        global segundaMatriz
        
        fila = int(self.fila_segunda_matriz.toPlainText())
        columna = int(self.columna_segunda_matriz.toPlainText())
        valor = int(self.valor_posicion_segunda_matriz.toPlainText())
        
        nuevo_valor = ArraysOperaciones.modificar_valor(segundaMatriz,fila,columna,valor)
        print(nuevo_valor)
        
    def boton_ejecutar(self):
        global primeraMatriz
        global segundaMatriz
        
        global filaMatriz1 
        global columnaMatriz1 
        global filaMatriz2 
        global columnaMatriz2 
        
        valor_operacion = self.operaciones.currentText() 
        
        if valor_operacion == "SUMA":
            if filaMatriz1 == filaMatriz2 and columnaMatriz1 == columnaMatriz2:
                producto_punto = str(ArraysOperaciones.suma(primeraMatriz,segundaMatriz))
                self.resultado.setText(producto_punto)
            else: 
                self.mostrar_notificacionSuma()
        elif valor_operacion == "RESTA":
            producto_punto = str(ArraysOperaciones.resta(primeraMatriz,segundaMatriz))
            self.resultado.setText(producto_punto)
        elif valor_operacion == "DIVISION":
            producto_punto = str(ArraysOperaciones.division(primeraMatriz,segundaMatriz))
            self.resultado.setText(producto_punto)
        elif valor_operacion == "MULTIPLICACION":
            if columnaMatriz1 == filaMatriz2: 
                producto_punto = str(ArraysOperaciones.multiplicacionPunto(primeraMatriz,segundaMatriz))
                self.resultado.setText(producto_punto)
                producto_punto2 = str(ArraysOperaciones.multiplicacionCruz(primeraMatriz,segundaMatriz))
                print("el resultado producto punto es: ",producto_punto2)
            else:
                self.mostrar_notificacionMultiplicacion()
                
    def mostrar_notificacionSuma(self):
        
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Advertencia")
        msg_box.setText("para hacer la suma el tamaño de las dos matrices deben ser iguales")
        msg_box.exec_()
    def mostrar_notificacionMultiplicacion(self):
        
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Advertencia")
        msg_box.setText("para la multiplicacion el numero de columas de la matriz 1 debe ser igual al numero de ilas de la matriz 2")
        msg_box.exec_()
                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.guardar_tamano_matrices.clicked.connect(ui.guardarMatriz)
    ui.guardar_valor_primera_matriz.clicked.connect(ui.guardarValor1)
    ui.guardar_valor_segunda_matriz.clicked.connect(ui.guardarValor2)
    ui.ejecutar.clicked.connect(ui.boton_ejecutar)
    Dialog.show()
    sys.exit(app.exec_())