from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QApplication
from ui_calculator import Ui_widget

import sys

class MyCalculator(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Llamar a la ventana
        self.show()
        
        # Titulo de la ventana
        self.setWindowTitle("Calculadora")
        
        # Definir posición y tamaño de la ventaa
        self.setGeometry(450,100,300,450)
        self.setMaximumHeight(450)
        self.setMaximumWidth(300)
        self.setMinimumHeight(450)
        self.setMinimumWidth(300)
    
        # Llamar a los botones
        self.btn_0.clicked.connect(self.on_button_click)
        self.btn_1.clicked.connect(self.on_button_click)
        self.btn_2.clicked.connect(self.on_button_click)
        self.btn_3.clicked.connect(self.on_button_click)
        self.btn_4.clicked.connect(self.on_button_click)
        self.btn_5.clicked.connect(self.on_button_click)
        self.btn_6.clicked.connect(self.on_button_click)
        self.btn_7.clicked.connect(self.on_button_click)
        self.btn_8.clicked.connect(self.on_button_click)
        self.btn_9.clicked.connect(self.on_button_click)
        self.btn_c.clicked.connect(self.on_button_click)
        self.btn_decimal.clicked.connect(self.on_button_click)
        self.btn_divide.clicked.connect(self.on_button_click)
        self.btn_igual.clicked.connect(self.on_button_click)
        self.btn_plus.clicked.connect(self.on_button_click)
        self.btn_multiply.clicked.connect(self.on_button_click)
        self.btn_minus.clicked.connect(self.on_button_click)

    def on_button_click(self):
        # Crear un metodo que reciba todas las señales de los botones en un solo objeto
        button = self.sender()

        # Crear una variable donde se almacenara los datos del Label de calculo
        current_text = self.main_label.text ()

        if current_text == "0":
            current_text = ""
        
        if button.text()== "=":

            #Excepciones
            try:
                resultado = str(eval(current_text))
                self.main_label.setText(resultado)
                self.main_label_2.setText(current_text + button.text())
            
            except ZeroDivisionError:
                self.main_label_2.setText("Error: Division por cero")
            except Exception as e:
                self.main_label_2.setText("Error: expresion invalida")
        
        else:
            self.main_label.setText(current_text + button.text())
                                
        if button.text() == "C":
            self.main_label.setText("0")
            self.main_label_2.setText("")



if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MyCalculator()
    window.show()
    app.exec()