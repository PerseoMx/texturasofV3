from PySide6.QtWidgets import QMainWindow, QTableWidgetItem,QDateEdit, QSlider, QMessageBox, QLabel
from PySide6.QtCore import QDate, Qt
from conectar import Conexion
from ui_textura import Ui_MainWindow
from calculadora import *

class myTextura(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("TextureSoft V3")

        #Instanciar la conexion a la base de datos
        self.bdTextura = Conexion()

        self.id_seleccionada = None

        #Conectar el evento de seleccion de la tabla
        self.table_datos.cellClicked.connect(self.seleccionar_fila)
        
        # Llamar a los botones del Menu
        self.btn_Calcular01.clicked.connect(self.inicio_to_calcularPage)
        self.btn_Calcular02.clicked.connect(self.inicio_to_calcularPage)

        self.btn_Triangulo01.clicked.connect(self.inicio_to_TrianguloPage)
        self.btn_Triangulo02.clicked.connect(self.inicio_to_TrianguloPage)

        self.btn_Metodo01.clicked.connect(self.inicio_to_MetodoPage)
        self.btn_Metodo02.clicked.connect(self.inicio_to_MetodoPage)

        self.btn_pH01.clicked.connect(self.inicio_to_pHPage)
        self.btn_pH02.clicked.connect(self.inicio_to_pHPage)

        self.btn_Soporte01.clicked.connect(self.inicio_to_SoportePage)
        self.btn_Soporte02.clicked.connect(self.inicio_to_SoportePage)
        
        #Llamar botones de calculo de textura
        self.btn_calcular_por.clicked.connect(self.calcular_cm)
        self.btn_calcular_textu.clicked.connect(self.calculo_textura)
        self.btn_guardar.clicked.connect(self.guardar_basedatos)
        self.btn_limpiar.clicked.connect(self.limpiar_datos)
        self.btn_eliminar.clicked.connect(self.eliminar_datos)
        self.btn_actualizar.clicked.connect(self.actualiza_misdatos)
        self.btn_buscar.clicked.connect(self.buscar)

        #cargar tabla al iniciar la APP
        self.cargar_tabla()

        # Llamar a Slider horizontal
        self.slider = self.findChild(QSlider, "horizontalSlider")
        self.slider.valueChanged.connect(self.slide_it)

        # Llamar boton de calculadora
        self.btn_calculator.clicked.connect(self.abrirCalculator)

        #Atributos para PH ordenando por Ph en los labels en una lista
        self.labels_ph = [self.lb_ph0, self.lb_ph01, self.lb_ph02, self.lb_ph03, self.lb_ph04,
                          self.lb_ph05, self.lb_ph06, self.lb_ph07, self.lb_ph08, self.lb_ph09,
                          self.lb_ph10, self.lb_ph11, self.lb_ph12, self.lb_ph13, self.lb_ph14]

    #FUNCIONES PARA PASAR CADA PAGINA DEL OBJETO STACKEDWIDGET

    def inicio_to_calcularPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def inicio_to_TrianguloPage(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def inicio_to_MetodoPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def inicio_to_pHPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def inicio_to_SoportePage(self):
        self.stackedWidget.setCurrentIndex(4)

    #FUCNION PARA CALCULAR TEXTURA

    def calculo_textura(self):

        #manejo de excepciones 

        try:
            # 1. introducir datos porcentuales de las partículas del suelo:
            arena = round(float(self.txt_ArenaPor.text()),2)
            arcilla = round(float(self.txt_ArcillaPor.text()),2)
            limo = round(float(self.txt_LimoPor.text()),2)

        except ValueError:
            QMessageBox.warning(self, "Error de datos", "Por favor, ingrese valores numericos válidos")
            return
        
        #2. validar que no existan números negativos
        if arena < 0 or arcilla < 0 or limo < 0:
            QMessageBox.warning(self, "Error de datos", "Los porcentajes no pueden ser negativos")
            return

        #3. Validar suma total con tolerancia de presición
        suma = round(arena + arcilla + limo,2)
        
        if suma !=100:
            QMessageBox.warning(self, "Error de datos", f"La suma de las partículas debe ser igual a 100 (Suma actual: {suma:.2f}%)")
            #self.txt_Total.setText(str(suma))
            return

        # Mostrar la suma correcta en el campo correspondiente
        self.txt_Total.setText(f"{suma:.2f}")
                             
        #4. Clasificación textural
        if (limo + 1.5 * arcilla) < 15:
            self.lab_textura.setText("ARENOSA")
                
        elif ((limo + 1.5* arcilla) >= 15) and ((limo + 2 * arcilla)) < 30:
            self.lab_textura.setText("ARENO FRANCO")
        
        elif ((arcilla >= 7 and arcilla < 20) and (arena > 52) and ((limo + 2 * arcilla) >= 30)) or (
                        arcilla < 7 and limo < 50 and ((limo + 2 * arcilla) >= 30)):
            self.lab_textura.setText("FRANCO ARENOSO")
                 
        elif ((arcilla >= 7 and arcilla < 27) and (limo >= 28 and limo < 50) and (arena <= 52)):
            self.lab_textura.setText("FRANCO")
    
    
        elif ((limo >= 50 and (arcilla >= 12 and arcilla < 27)) or ((limo >= 50 and limo < 80) and arcilla < 12)):
            self.lab_textura.setText("FRANCO LIMOSA")
        
        elif (limo >= 80 and arcilla < 12):
            self.lab_textura.setText("LIMOSA")
             
        elif ((arcilla >= 20 and arcilla < 35) and (limo < 28) and (arena > 45)):
            self.lab_textura.setText("FRANCO ARCILLO ARENOSA")
        
        elif ((arcilla >= 27 and arcilla < 40) and (arena > 20 and arena <= 45)):
            self.lab_textura.setText("FRANCO ARCILLOSA")
        
        elif ((arcilla >= 27 and arcilla < 40) and (arena <= 20)):
            self.lab_textura.setText("FRANCO ARCILLO LIMOSA")
        
        elif (arcilla >= 35 and arena > 45):
            self.lab_textura.setText("ARCILLO ARENOSA")
      
        elif (arcilla >= 40 and limo >= 40):
            self.lab_textura.setText("ARCILLO LIMOSA")
              
        elif (arcilla >= 40 and arena <= 45 and limo < 40):
            self.lab_textura.setText("ARCILLOSA")
    
        else:
            self.lab_textura.setText("VALOR FUERA DE RANGO")
            
    
    def calcular_cm(self):

            
        try:
        #Variables de datos en Cm

            arcilla_cm = float(self.txt_Arcilla.text())
            arena_cm = float(self.txt_Arena.text())
            limo_cm = float(self.txt_Limo.text())

        except ValueError:
            QMessageBox.warning(self, "Error de datos", "Por favor, ingrese valores numericos válidos en cm")
            #self.lab_textura.setText("Por favor, ingrese valores numericos válidos en cm")
            return
        
        #2. validar que no existan números negativos
        if arena_cm < 0 or arcilla_cm < 0 or limo_cm < 0:
            QMessageBox.warning(self, "Error de datos", "Los valores no pueden ser negativos")
            #self.lab_textura.setText("Los valores no pueden ser negativos")
            return
        #Suma del total de cm de arena, arcilla y limo
        suma_cm = arcilla_cm + arena_cm + limo_cm
        
        if suma_cm <=0:
            QMessageBox.warning(self, "Error de datos", "La suma de las medidas en cm debe ser mayor a 0")
            #self.lab_textura.setText("La suma de las medidas en cm debe ser mayor a 0")
            return
        
        #calculo de porcentajes de arena, arcilla y limo a partir de las mediciones en Cm
        arcilla_por = round((arcilla_cm / suma_cm * 100),2)
        arena_por = round((arena_cm / suma_cm * 100), 2)
        # El limo absorbe el residuo del redondeo para asegurar suma = 100.00% exacto
        limo_por = round(100.0 - (arcilla_por + arena_por), 2)
        
        #introducir los resultados en porciento a los campos de particulas en %
        self.txt_TotalCm.setText(f"{suma_cm:.2f}")

        self.txt_ArenaPor.setText(str(arena_por))
        self.txt_ArcillaPor.setText(str(arcilla_por))
        self.txt_LimoPor.setText(str(limo_por))

        #ejecuta clasificacion
        self.calculo_textura()

    def guardar_basedatos(self):
        # registrar los datos a la bse de datos que se encuentran en los campos de texto
        nombre = self.txt_nombre.text().strip().upper()
        lote = self.txt_lote.text().strip().upper()
        fecha = self.date_fecha.date().toString("dd-MM-yyyy")
        arena_cm = self.txt_Arena.text()
        arcilla_cm = self.txt_Arcilla.text()
        limo_cm = self.txt_Limo.text()
        total_cm = self.txt_TotalCm.text()
        arena_por = self.txt_ArenaPor.text()
        arcilla_por = self.txt_ArcillaPor.text()
        limo_por = self.txt_LimoPor.text()
        total_por = self.txt_Total.text()
        textura = self.lab_textura.text().strip().upper()

        #insertar los datos obligatorios y validacion de datos asegurandose que se ingrese los datos a la base de datos
        if nombre and lote and textura:
            self.bdTextura.insertar_datos(nombre, lote, fecha, arena_cm, arcilla_cm, limo_cm, total_cm, 
                                          arena_por, arcilla_por, limo_por, total_por, textura)
            QMessageBox.information(self, "Información", "Datos registrados en la base de datos")

        else:
            if nombre =="":
                QMessageBox.information(self, "Information", "Debe llenar el campo 'Nombre'")
            elif lote =="" and textura =="":
                QMessageBox.information(self, "Information", "Debe llenar los campos 'lote/parcela'")
            elif lote == "":
                QMessageBox.information(self, "Information", "Debe llenar el campo 'Lote/parcela'")
            elif textura =="":
                QMessageBox.information(self, "Information", "Debe determinar la textura del suelo para que se registre en la base de datos")

        self.cargar_tabla()

    #Mostrar datos en la tabla
    def cargar_tabla(self):
        datos = self.bdTextura.mostrar_datos()

        self.table_datos.setRowCount(0) #Limpiar la tabla antes de llenarla

        for fila, muestra in enumerate(datos):
            self.table_datos.insertRow(fila)

            self.table_datos.setItem(fila, 0, QTableWidgetItem(str(muestra[0])))
            self.table_datos.setItem(fila, 1, QTableWidgetItem(muestra[1]))
            self.table_datos.setItem(fila, 2, QTableWidgetItem(muestra[2]))
            self.table_datos.setItem(fila, 3, QTableWidgetItem(muestra[3]))
            self.table_datos.setItem(fila, 4, QTableWidgetItem(str(muestra[8])))
            self.table_datos.setItem(fila, 5, QTableWidgetItem(str(muestra[9])))
            self.table_datos.setItem(fila, 6, QTableWidgetItem(str(muestra[10])))
            self.table_datos.setItem(fila, 7, QTableWidgetItem(muestra[12]))

    def seleccionar_fila(self, fila, columna):

        #Seleccionar el registro a partir de la fila de la QTable
        self.txt_nombre.setText(self.table_datos.item(fila, 1).text())
        fecha_qdate = QDate.fromString(self.table_datos.item(fila, 2).text(), "dd-MM-yyyy")
        self.date_fecha.setDate(fecha_qdate)
        self.txt_lote.setText(self.table_datos.item(fila, 3).text())
        self.txt_ArenaPor.setText(self.table_datos.item(fila, 4).text())
        self.txt_ArcillaPor.setText(self.table_datos.item(fila, 5).text())
        self.txt_LimoPor.setText(self.table_datos.item(fila, 6).text())
        self.lab_textura.setText(self.table_datos.item(fila, 7).text())

        #Seleccionar los registros faltantes a partir de la base de datos
        #obtener el id de la fila clickeada
        self.id_seleccionada = int(self.table_datos.item(fila, 0).text())
        #consultar la base de datos con la id que se obtiene en una tupla
        registro_completo = self.bdTextura.mostrar_datos_por_id(self.id_seleccionada)
        
        #de la tupla se saca el dato que se necesita por su indice de la base de datos

        self.txt_Arena.setText(str(registro_completo[4]))
        self.txt_Arcilla.setText(str(registro_completo[5]))
        self.txt_Limo.setText(str(registro_completo[6]))
        self.txt_TotalCm.setText(str(registro_completo[7]))
        self.txt_Total.setText(str(registro_completo[11]))

        
    def actualiza_misdatos(self):
        
        #condicion para que esté seleccionado una fila para actualizar, esa fila seleccionada esta liga al Id
        if self.id_seleccionada is None:
            QMessageBox.information(self, "Información", "Seleccione un registro de la tabla para actualizar")
            return
        
        
        nombre = self.txt_nombre.text().strip().upper()
        lote = self.txt_lote.text().strip().upper()
        fecha = self.date_fecha.date().toString("dd-MM-yyyy")
        arena_cm = self.txt_Arena.text()
        arcilla_cm = self.txt_Arcilla.text()
        limo_cm = self.txt_Limo.text()
        total_cm = self.txt_TotalCm.text()
        arena_por = self.txt_ArenaPor.text()
        arcilla_por = self.txt_ArcillaPor.text()
        limo_por = self.txt_LimoPor.text()
        total_por = self.txt_Total.text()
        textura = self.lab_textura.text().strip().upper()

        #insertar los datos obligatorios y validacion de datos asegurandose que se ingrese los datos a la base de datos
        if nombre and lote and textura:
            self.bdTextura.actualizar_datos(self.id_seleccionada, nombre, fecha, lote, arena_cm, arcilla_cm, limo_cm, total_cm, 
                                          arena_por, arcilla_por, limo_por, total_por, textura)
            QMessageBox.information(self, "Información", "Datos actualizado en la base de datos")

            self.limpiar_datos()
            self.cargar_tabla()
            
        else:
            if nombre =="":
                QMessageBox.information(self, "Information", "Debe llenar el campo 'Nombre'")
            elif lote =="" and textura =="":
                QMessageBox.information(self, "Information", "Debe llenar los campos 'lote/parcela'")
            elif lote == "":
                QMessageBox.information(self, "Information", "Debe llenar el campo 'Lote/parcela'")
            elif textura =="":
                QMessageBox.information(self, "Information", "Debe determinar la textura del suelo para que se actualice en la base de datos")


    
    def limpiar_datos(self):

        self.txt_nombre.clear()
        self.txt_lote.clear()
        self.txt_Arena.clear()
        self.txt_Arcilla.clear()
        self.txt_Limo.clear()
        self.txt_TotalCm.clear()
        self.txt_ArenaPor.clear()
        self.txt_ArcillaPor.clear()
        self.txt_LimoPor.clear()
        self.txt_Total.clear()
        self.lab_textura.clear()
        self.txt_buscar.clear()

        # dejar el valor Cero por defecto en los campos especificos

        self.txt_Arena.setText("0")
        self.txt_Arcilla.setText("0")
        self.txt_Limo.setText("0")
        self.txt_ArenaPor.setText("0")
        self.txt_ArcillaPor.setText("0")
        self.txt_LimoPor.setText("0")
        
        
        #cargar los datos de la tabla
        self.cargar_tabla()

        #reinicia el Id
        self.id_seleccionada=None

    
    def eliminar_datos(self):
        #Obtener el número de fila seleccionada en la tabla (-1 si no hay ninguna)
        fila = self.table_datos.currentRow()

        if fila == -1:
            # No hay ninguna fila seleccionada
            QMessageBox.information(self,"Información", "Seleccione un dato en la tabla para eliminar")
        else:
            #Leer la id del dato desde la columna 0 de a fila seleccionada
            item_id = self.table_datos.item(fila,0)
            id_textura = item_id.text()

            #pedir confirmación al usuario antes de eliminar:
            respuesta = QMessageBox.question(self, "Confirmar", "Seguro que quiere eliminar este dato?")

            if respuesta == QMessageBox.Yes:
                # El usuario confirmó: eliminar de la base de datos
                self.bdTextura.eliminar_datos(id_textura)
                # Refrescar la tabla para reflejar el cambio
                self.cargar_tabla()
                # Avisar al usuario que la eliminación fue exitosa
                QMessageBox.information(self, "Información","Se eliminó correctamente el dato, y se actualizó la tabla")

            else:
                # El usuario canceló la eliminación    
                QMessageBox.information(self, "Información","No se eliminó ningún dato")

    def buscar(self):
        nombre_dato = self.txt_buscar.text().upper()
        datos = self.bdTextura.buscar_datos(nombre_dato)

        #limpiar tabla y volver a llenarla pero solo con los resultados de la busqueda
        self.table_datos.setRowCount(0)

        if datos:
            for fila, muestra in enumerate(datos):

                self.table_datos.insertRow(fila)

                self.table_datos.setItem(fila, 0, QTableWidgetItem(str(muestra[0])))
                self.table_datos.setItem(fila, 1, QTableWidgetItem(muestra[1]))
                self.table_datos.setItem(fila, 2, QTableWidgetItem(muestra[2]))
                self.table_datos.setItem(fila, 3, QTableWidgetItem(muestra[3]))
                self.table_datos.setItem(fila, 4, QTableWidgetItem(str(muestra[8])))
                self.table_datos.setItem(fila, 5, QTableWidgetItem(str(muestra[9])))
                self.table_datos.setItem(fila, 6, QTableWidgetItem(str(muestra[10])))
                self.table_datos.setItem(fila, 7, QTableWidgetItem(muestra[12]))

            QMessageBox.information(self, "Información", f"Se encontraron {len(datos)} datos de muestreos")
        else:
            QMessageBox.information(self, "Información", "No Se encontraron los datos de muestreos")

    #FUNCION PARA DETERMINAR EL PH POR COLORIMETRÍA

    def slide_it(self, value):

             
        # Enviar al Label el valor cuando recorre el Slide Horizontal, en la linea se formateo para que "pH" se muestre en el Label
        self.lb_pH.setText(f"pH: {str(value)}")
        
        # Centrar los labeles de salida de pH
        self.lb_pH.setAlignment(Qt.AlignCenter)
        self.lb_pH_Resultado.setAlignment(Qt.AlignCenter)

        #El ciclo for quita los colores a todos los labeles en cada vuelta del ciclo       
        for elemento in self.labels_ph:
            elemento.setStyleSheet("background-color: none")

        # Expresar el rango de ph de forma literal en el label en función al recorrer el Slide
        if self.lb_pH.text() =="pH: 0" or self.lb_pH.text() =="pH: 1" :
            self.lb_pH_Resultado.setText("Muy ácido")
            #pinta de color los labeles que corresponden con el pH
            self.lb_ph0.setStyleSheet("background-color:rgb(255,0,0)")
            self.lb_ph01.setStyleSheet("background-color: rgb(244, 106, 7)")
            
        elif self.lb_pH.text() =="pH: 2" or self.lb_pH.text() =="pH: 3" or self.lb_pH.text() =="pH: 4":
            self.lb_pH_Resultado.setText("Moderadamente ácido")
            
            #pinta de color los labeles que corresponden con el pH
            self.lb_ph02.setStyleSheet("background-color:rgb(251,199,1)")
            self.lb_ph03.setStyleSheet("background-color: rgb(244, 239,0)")
            self.lb_ph04.setStyleSheet("background-color:rgb(180, 213,0)")
                    
        elif self.lb_pH.text() =="pH: 5" or self.lb_pH.text() =="pH: 6":
            self.lb_pH_Resultado.setText("Ligeramente ácido")

            #pinta de color los labeles que corresponden con el pH
            self.lb_ph05.setStyleSheet("background-color:rgb(130,194,45)")
            self.lb_ph06.setStyleSheet("background-color: rgb(74,184,61)")
                    
        elif self.lb_pH.text()=="pH: 7":
            self.lb_pH_Resultado.setText("Neutro")

            #pinta de color los labeles que corresponden con el pH
            self.lb_ph07.setStyleSheet("background-color:rgb(6,169,63)")
                    
        elif self.lb_pH.text() =="pH: 8" or self.lb_pH.text() =="pH: 9":
            self.lb_pH_Resultado.setText("Ligeramente Alcalino")

            #pinta de color los labeles que corresponden con el pH
            self.lb_ph08.setStyleSheet("background-color:rgb(26,182,101)")
            self.lb_ph09.setStyleSheet("background-color: rgb(0,186,181)")
                         
        
        elif self.lb_pH.text() =="pH: 10" or self.lb_pH.text() =="pH: 11" or self.lb_pH.text() =="pH: 12":
            self.lb_pH_Resultado.setText("Moderadamente alcalino")

            #pinta de color los labeles que corresponden con el pH
            self.lb_ph10.setStyleSheet("background-color:rgb(65,143,205)")
            self.lb_ph11.setStyleSheet("background-color: rgb(55,81,168)")
            self.lb_ph12.setStyleSheet("background-color:rgb(90,80,166)")
            
                    
        elif self.lb_pH.text() =="pH: 13" or self.lb_pH.text() =="pH: 14":
            self.lb_pH_Resultado.setText("Muy Alcalino")

            #pinta de color los labeles que corresponden con el pH
            self.lb_ph13.setStyleSheet("background-color:rgb(97,68,160)")
            self.lb_ph14.setStyleSheet("background-color: rgb(70,41,134)")
            
            

# FUNCION PARA ABRIR LA VENTANA CALCULADORA
    def abrirCalculator(self):
        self.ventana_calculator = MyCalculator()
        self.ventana_calculator.show()

