import os
import re
from pymongo_the_sql.pymongo_the_sql import PyMongoTheSql
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

        ast = self.parser.parse(data)
        # Manejar los resultados del análisis sintáctico
        self.handle_syntax_tree(ast)

        # Convertir el AST a consulta MongoDB
        mongo_query = self.convert_ast_to_mongo_query(ast)

        # Mostrar la consulta MongoDB en el área de resultado
        self.ventana.escribirAreaResultado(str(mongo_query))

    # Función para manejar los resultados del análisis sintáctico
    def handle_syntax_tree(self, ast):
        if ast is not None:
            # Imprimir el árbol de sintaxis abstracta en el área de texto
            self.ventana.escribirAreaFileError(str(ast))
        else:
            # Si el análisis sintáctico falló, mostrar un mensaje de error
            self.ventana.escribirAreaFileError("Error de sintaxis: no se pudo construir el árbol de sintaxis abstracta.")

    def convert_ast_to_mongo_query(self, ast):
        if not isinstance(ast, tuple) or len(ast) != 3:
            return "Consulta inválida"

        if ast[0] != 'SELECT':
            return "Consulta no es un SELECT válido"

        columns = ast[1]
        table = ast[2]

        # Crear una instancia de PyMongoTheSql para la conversión
        pymongo_the_sql = PyMongoTheSql()

        try:
            # Realizar la conversión utilizando la clase PyMongoTheSql
            mongo_query = pymongo_the_sql.convert_to_mongo_query(columns, table)
            return mongo_query
        except Exception as e:
            return f"Error durante la conversión: {str(e)}"

    def convert_to_mongo_query(self, columns, table):
        # Implementa aquí la lógica para convertir las columnas y la tabla a una consulta MongoDB en MQL
        # El argumento 'columns' debe ser un diccionario con las columnas y cláusulas WHERE si las hay
        # El argumento 'table' debe ser el nombre de la tabla en la consulta SQL

        # Aquí solo se muestra un ejemplo básico de la conversión para una consulta SELECT simple
        # Es posible que necesites extender esta lógica para cubrir más casos y condiciones
        mongo_query = {'collection': table}

        if 'SELECT' in columns:
            projection = {column: 1 for column in columns['SELECT']}
            mongo_query['projection'] = projection

        if 'WHERE' in columns:
            where_clause = columns['WHERE']
            where_mql = self.convert_condition_to_mql(where_clause)
            mongo_query['filter'] = where_mql

        return mongo_query
    
    def convert_condition_to_mql(self, condition):
        # Implementa aquí la lógica para convertir la condición WHERE a una consulta MongoDB en MQL
        # Esta implementación es simplificada y solo cubre comparaciones básicas
        # Necesitarás ajustarla según tus necesidades y para manejar otros operadores y condiciones

        if not isinstance(condition, tuple) or len(condition) != 3:
            return {}

        operator = condition[0]
        left_operand = condition[1]
        right_operand = condition[2]

        # Convertir los operandos según sea necesario
        # Implementar las conversiones para tus columnas específicas
        if left_operand == 'column3':
            left_operand = 'campo3'
        elif left_operand == 'column4':
            left_operand = 'campo4'

        if isinstance(right_operand, str) and right_operand.isdigit():
            right_operand = int(right_operand)

        # Realizar la conversión de operadores
        if operator == '=':
            return {left_operand: right_operand}
        elif operator == '>':
            return {left_operand: {'$gt': right_operand}}
        elif operator == '<':
            return {left_operand: {'$lt': right_operand}}
        # Agregar más conversiones de operadores según sea necesario...

        return {}