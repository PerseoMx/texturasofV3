import sqlite3

class Conexion():

    def __init__(self):

        #crear y conectar la base de datos
        self.miConexion = sqlite3.connect("bd_textura.db")

        #crear cursor
        self.miCursor = self.miConexion.cursor()

        #crear la tabla datos_textura en caso no exista

        self.miCursor.execute("""
            CREATE TABLE IF NOT EXISTS datos_textura(
                id_textura INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(150),
                fecha DATE,
                lote VARCHAR(50),
                arena_cm DECIMAL(10,2),
                arcilla_cm DECIMAL(10,2),
                limo_cm DECIMAL(10,2),
                total_cm DECIMAL(10,2),
                arena_por DECIMAL(10,2),
                arcilla_por DECIMAL(10,2),
                limo_por DECIMAL(10,2),
                total_por DECIMAL(10,2),
                textura VARCHAR(50)                
            )

        """)
        #confirmar los cambios
        self.miConexion.commit()

    #Funcion insertar datos
    def insertar_datos(self, nombre, lote, fecha,  arena_cm, arcilla_cm, limo_cm, total_cm, arena_por, arcilla_por, limo_por, total_por, textura):
        miCursor = self.miConexion.cursor()

        #insertar datos en los campos de texto
        miCursor.execute("""INSERT INTO datos_textura(nombre, fecha, lote, arena_cm, arcilla_cm,
            limo_cm, total_cm, arena_por, arcilla_por, limo_por, total_por, textura)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",
            (nombre, fecha, lote, arena_cm, arcilla_cm, limo_cm, total_cm, arena_por, arcilla_por, limo_por, total_por, textura))

        self.miConexion.commit()
        nuevo_id = miCursor.lastrowid #<--- guarda el id antes de cerrar
        miCursor.close()
        return nuevo_id

    #funcion mostrar datos
    def mostrar_datos(self):
        miCursor = self.miConexion.cursor()

        miCursor.execute("SELECT * FROM datos_textura")
        datos = miCursor.fetchall()

        miCursor.close()
        return datos
    
    #funcion mostrar datos por id:
    def mostrar_datos_por_id(self, id_textura):
        miCursor = self.miConexion.cursor()

        miCursor.execute("SELECT * FROM datos_textura WHERE id_textura = ?", (id_textura,))
        datos = miCursor.fetchone()

        miCursor.close()
        return datos


    #funcion eliminar datos
    def eliminar_datos(self, id_textura):

        miCursor = self.miConexion.cursor()

        miCursor.execute("DELETE FROM datos_textura WHERE id_textura=?", (id_textura,))
        self.miConexion.commit()
        miCursor.close()

    #funcion actualizar datos
    def actualizar_datos(self, id_textura, nombre, fecha, lote, arena_cm, arcilla_cm, limo_cm, total_cm, arena_por, arcilla_por, limo_por, total_por, textura):
        miCursor = self.miConexion.cursor()

        miCursor.execute("""
            UPDATE datos_textura
            SET nombre=?, fecha=?, lote=?, arena_cm=?, arcilla_cm=?, limo_cm=?, total_cm=?, arena_por=?, arcilla_por=?, limo_por=?, total_por=?, textura=?
            WHERE id_textura = ?
        """, (nombre, fecha, lote, arena_cm, arcilla_cm, limo_cm, total_cm, arena_por, arcilla_por, limo_por, total_por, textura, id_textura))

        fila_actualizada = miCursor.rowcount
        self.miConexion.commit()
        miCursor.close()
        return fila_actualizada

    #funcion para buscar datos
    def buscar_datos(self,nombre):
        miCursor = self.miConexion.cursor()

        patron = f"%{nombre}%" #aqui se establece el patrón de busqueda
        miCursor.execute("SELECT * FROM datos_textura WHERE nombre LIKE ?", (patron,))
        resultado = miCursor.fetchall()
        
        miCursor.close()
        return resultado
        