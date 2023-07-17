from modelos_Dts.Aritmeticos import dt_aritmeticos, dt_esAritmetico
'''
from modelos_DTs.Entero import dt_Entero, dt_esDigito
from modelos_DTs.Relacionales import dt_relacionales, dt_esRelacional
from modelos_DTs.Logicos import dt_logicos, dt_esLogico
from modelos_DTs.Delimitadores import dt_esDelimitador
from modelos_DTs.Resto_del_Mundo import dt_restoMundo, dt_esRestoMundo
from modelos_DTs.identificadores import dt_esLetra, dt_esIdentificador, dt_identificadores
from modelos_DTs.cadenas import dt_esCadena, dt_cadenas
from modelos_DTs.comentarios import dt_esComentario, 
'''

class Dts:

    ##
    # Constructor
    # @Param marshall: referencia de memoria del objeto marshall
    # @Param pr: referencia de memoria del objeto pr
    ##
    def __init__(self, marshall, pr):
        self.marshall = marshall
        self.pr = pr

    
    '''
    Metodo para ver si un elemto pertenece a una Lista
    mediante un ForEach
        @Param lista: lista en la cual se hara la busqueda
        @Param elemento: elemento a buscar en la lista
        @Return Bolean: True si pertenece, False si no
    '''
    def perteneceLista(self, caracter, lista):
        for elemento in lista:
            if caracter == str(elemento):
                return True

        return False
    

    '''
    Metodo para reconocer si un caracter es Aritmetico
        @param: caracter a evaluar
        @Return: True si es aritmetico, False si no
    '''
    def esAritmetico(self, caracter):
        return dt_esAritmetico( self, caracter )

    '''
    Diagrama de Transicion Aritmeticos
        @Return: diccionario con  token y lexema
                acorde a la respuesta
    '''
    def aritmeticos(self, lexema):
        return dt_aritmeticos(self, lexema)