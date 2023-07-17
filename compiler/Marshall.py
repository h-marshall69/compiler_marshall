import os
import re
from compiler.lex import *
from compiler.parser_1 import *

class Marshall:

    def __init__(self, ventana):

        # Inyeccion de Dependencias
        self.ventana = ventana
        self.lexer = lex.lex()
        self.parser = yacc.yacc()

    def iniciaCompilaicon(self):


        data = self.ventana.getTextAreaFuente()
        dataLexema = ""

        self.lexer.input(data)

        while True:
            tok = self.lexer.token()
            if not tok: 
                break      # No more input
            dataLexema += str(tok.type) + ' ' + str(tok.value) + ' ' + str(tok.lineno) + ' ' + str(tok.lexpos) + '\n'

        self.ventana.escribirAreaLexema(dataLexema)
        #self.parser.parse(data)
