from presentacion.Uami import Uami

class Main:

    def __init__(self, txt):
        self.txtAreaFuente = txt

    def iniciarCompilacion(self):
        uami = Uami(self)
        uami.iniciaCompilacion()

    def getTextAreaFuente(self):
        return self.getTextAreaFuente

prueba = Main("SELECT * FROM Usuarios;")