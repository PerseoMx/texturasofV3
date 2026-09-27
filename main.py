from PySide6.QtWidgets import QApplication
from logica import myTextura
import sys


app= QApplication(sys.argv)
window = myTextura()
window.show()
app.exec()