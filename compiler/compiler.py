import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QFileDialog, QMessageBox, QTextEdit, QLabel, QApplication
from PyQt5 import QtGui
from compiler.Marshall import Marshall

class Ventana(QMainWindow):

    # Creamos una subclase de QWidget para nuestra ventana
    def __init__(self):
        super().__init__()

        # Direccion Url del archivo fuente
        self.fuenteUrl = ""

        # Configuracion de la ventana
        self.setWindowTitle('Mi Ventana')  # Establecemos el título de la ventana
        self.setGeometry(250, 50, 880, 670)  # Establecemos la posición y el tamaño de la ventana
        self.setWindowTitle("Marshall") # Titulo de La ventana
        self.setWindowIcon(QtGui.QIcon("img/logo.png"))

        # Evento para compilar
        self.EventoCompilar = QAction(QtGui.QIcon("img/comp.png"), 'compilar', self)
        self.EventoCompilar.setShortcut("Ctrl+R")
        self.EventoCompilar.setStatusTip('Iniciar la compilacion')
        self.EventoCompilar.triggered.connect(self.iniciarCompilacion)

        # Configuracion del Menu Principal
        self.MenuPrincipal = self.menuBar()

        # Se crea el menu archivo y se agregan los eventos
        self.MenuArchivo = self.MenuPrincipal.addMenu('&Archivo')
        self.MenuArchivo.addAction(self.EventoCompilar)

        # Se crea el Toolbar y se agregan los eventos
        self.ToolBar = self.addToolBar("Archivo")
        self.ToolBar.addAction(self.EventoCompilar)

        self.diseno()

    def diseno(self):

        # Caja de texto (text Areas)
        self.txtAreaFuente = QTextEdit(self)
        self.txtAreaFuente.setGeometry(10, 85, 425, 270)

        self.txtAreaLexema = QTextEdit(self)
        self.txtAreaLexema.setGeometry(445, 85, 425, 270)

        self.txtAreaFileError = QTextEdit(self)
        self.txtAreaFileError.setGeometry(10, 380, 425, 270)

        self.txtAreaResultado = QTextEdit(self)
        self.txtAreaResultado.setGeometry(445, 380, 425, 270)


        # Etiquetas (Labels)
        self.lbl_Fuente = QLabel("CONTENIDO DEL ARCHIVO FUENTE: ", self)
        self.lbl_Fuente.setGeometry(80, 40, 300, 60)
        self.lbl_Fuente.setFont(QtGui.QFont('SansSerif', 11))

        self.lbl_fileError = QLabel("ANALIZADOR SINTACTICO: ", self)
        self.lbl_fileError.setGeometry(80, 335, 300, 60)
        self.lbl_fileError.setFont(QtGui.QFont('SansSerif', 11))

        self.lbl_compilacion = QLabel("RESULTADO DE LA COMPILACION: ", self)
        self.lbl_compilacion.setGeometry(550, 335, 300, 60)
        self.lbl_compilacion.setFont(QtGui.QFont('SansSerif', 11))

        self.lbl_fileLexico = QLabel("ANALIZADOR LEXICO: ", self)
        self.lbl_fileLexico.setGeometry(550, 40, 300, 60)
        self.lbl_fileLexico.setFont(QtGui.QFont('SansSerif', 11))
        self.show()

    def escribirAreaFuente(self, texto):
        self.txtAreaFuente.setText(texto)

    def getTextAreaFuente(self):
        return self.txtAreaFuente.toPlainText()
    
    def escribirAreaLexema(self, texto):
        self.txtAreaLexema.setText( texto )

    def escribirAreaFileError(self, texto):
        self.txtAreaFileError.setText( texto )

    def escribirAreaResultado(self, texto):
        self.txtAreaResultado.setText( texto )
    
    def getTextAreaLexema(self):
        return self.txtAreaLexema.toPlainText()

    def iniciarCompilacion(self):
        marshall = Marshall(self)
        marshall.iniciaCompilaicon()