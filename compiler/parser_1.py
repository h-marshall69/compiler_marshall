import ply.yacc as yacc
from compiler.lex import tokens

# Reglas de gramática para un subconjunto de sentencias SQL
def p_statement(p):
    '''statement : select_statement
                 | insert_statement
                 | update_statement
                 | delete_statement'''
    p[0] = p[1]

def p_select_statement(p):
    '''select_statement : SELECT columns FROM table
                        | SELECT columns FROM table where_clause'''
    if len(p) == 5:
        p[0] = ('SELECT', p[2], p[4])
    else:
        p[0] = ('SELECT', p[2], p[4], p[5])

def p_insert_statement(p):
    '''insert_statement : INSERT INTO table LPAREN columns RPAREN VALUES LPAREN values RPAREN'''
    p[0] = ('INSERT', p[3], p[5], p[8])

def p_update_statement(p):
    '''update_statement : UPDATE table SET assignments where_clause'''
    p[0] = ('UPDATE', p[2], p[4], p[5])

def p_delete_statement(p):
    '''delete_statement : DELETE FROM table where_clause'''
    p[0] = ('DELETE', p[3], p[4])

def p_columns(p):
    '''columns : ID
               | ID COMMA columns'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_values(p):
    '''values : value
              | value COMMA values'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_assignments(p):
    '''assignments : ID EQ value
                   | ID EQ value COMMA assignments'''
    if len(p) == 4:
        p[0] = {p[1]: p[3]}
    else:
        p[0] = {p[1]: p[3], **p[5]}

def p_table(p):
    '''table : ID'''
    p[0] = p[1]

def p_where_clause(p):
    '''where_clause : WHERE condition'''
    p[0] = p[2]

def p_condition(p):
    '''condition : comparison_condition
                 | logical_condition'''
    p[0] = p[1]

def p_comparison_condition(p):
    '''comparison_condition : value EQ value
                            | value NEQ value
                            | value LE value
                            | value GE value
                            | value LT value
                            | value GT value'''
    p[0] = (p[2], p[1], p[3])

def p_logical_condition(p):
    '''logical_condition : condition AND condition
                         | condition OR condition
                         | NOT condition'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = ('NOT', p[2])

def p_value(p):
    '''value : NUMBER
             | FLOAT
             | STRING
             | ID'''
    p[0] = p[1]

# Definir una regla para manejar errores de sintaxis
def p_error(p):
    if p:
        print(f"Error de sintaxis en el token '{p.value}' en la posición {p.lexpos}")
    else:
        print("Error de sintaxis al final de la entrada")

# Construir el analizador sintáctico
parser = yacc.yacc()

# Función para analizar una sentencia SQL
def parse_sql(input_string):
    return parser.parse(input_string)

# Prueba del analizador sintáctico
data = """
SELECT column1, column2 FROM table_name WHERE column3 = 'value' AND column4 > 100;
INSERT INTO table_name (column1, column2) VALUES ('value1', 'value2');
UPDATE table_name SET column1 = 10, column2 = 20 WHERE column3 = 'value3';
DELETE FROM table_name WHERE column1 = 5;
"""

# Separar las sentencias SQL y eliminar líneas vacías
statements = [stmt.rstrip() for stmt in data.strip().split(';') if stmt.strip()]
for statement in statements:
    result = parse_sql(statement)
    print(result)