import ply.yacc as yacc
from lexer import tokens

# Reglas de la gramática
def p_insert_statement(p):
    '''
    insert_statement : INSERT INTO IDENTIFIER LPAREN column_list RPAREN VALUES LPAREN value_list RPAREN
    '''
    p[0] = ("INSERT", p[3], p[5], p[9])

def p_column_list(p):
    '''
    column_list : IDENTIFIER
                | column_list COMMA IDENTIFIER
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_value_list(p):
    '''
    value_list : value
               | value_list COMMA value
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_value(p):
    '''
    value : STRING
          | NUMBER
          | NULL
    '''
    p[0] = p[1]

# Regla de la gramática para SELECT
def p_select_statement(p):
    '''
    select_statement : SELECT select_list FROM table_expression
    '''
    p[0] = (p[1], p[2], p[4])

def p_select_list(p):
    '''
    select_list : select_item
                | select_list COMMA select_item
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_select_item(p):
    '''
    select_item : IDENTIFIER
                | IDENTIFIER AS IDENTIFIER
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[3])

def p_table_expression(p):
    '''
    table_expression : IDENTIFIER
                     | table_expression COMMA IDENTIFIER
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


# Regla para manejar errores sintácticos
def p_error(p):
    if p:
        print("Error de sintaxis en la entrada en la posición", p)
    else:
        print("Error de sintaxis en la entrada")

# Construir el analizador sintáctico
parser = yacc.yacc()

# Prueba del analizador sintáctico
data = "INSERT INTO table_name (column1, column2) VALUES ('value1', 123)"
data1 = "SELECT * FROM table_name;"
result = parser.parse(data)
print(result)
