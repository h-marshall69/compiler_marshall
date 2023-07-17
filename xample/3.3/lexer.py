import ply.lex as lex

# Definición de los tokens
tokens = [
    'SELECT',
    'INSERT',
    'UPDATE',
    'DELETE',
    'FROM',
    'INTO',
    'VALUES',
    'SET',
    'WHERE',
    'AND',
    'OR',
    'NOT',
    'AS',
    'IDENTIFIER',
    'STRING',
    'NUMBER',
    'NULL',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'SEMICOLON'
]

# Expresiones regulares para los tokens
def t_SELECT(t):
    r'SELECT'
    return t

def t_INSERT(t):
    r'INSERT'
    return t

def t_UPDATE(t):
    r'UPDATE'
    return t

def t_DELETE(t):
    r'DELETE'
    return t

def t_FROM(t):
    r'FROM'
    return t

def t_INTO(t):
    r'INTO'
    return t

def t_VALUES(t):
    r'VALUES'
    return t

def t_SET(t):
    r'SET'
    return t

def t_WHERE(t):
    r'WHERE'
    return t

def t_AND(t):
    r'AND'
    return t

def t_OR(t):
    r'OR'
    return t

def t_NOT(t):
    r'NOT'
    return t

def t_AS(t):
    r'AS'
    return t

def t_STRING(t):
    r'\'[^\']*\''
    return t

def t_NUMBER(t):
    r'\d+'
    return t

def t_NULL(t):
    r'NULL'
    return t

def t_COMMA(t):
    r','
    return t

def t_LPAREN(t):
    r'\('
    return t

def t_RPAREN(t):
    r'\)'
    return t

def t_SEMICOLON(t):
    r';'
    return t

# Expresión regular para el token IDENTIFIER
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Ignorar espacios y saltos de línea
t_ignore = ' \n'

# Función para manejar errores léxicos
def t_error(t):
    print("Caracter ilegal:", t.lexpos)
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()


# Prueba del analizador léxico
if __name__ == '__main__':
    data = "SELEC column1, column2 FROM table_name WHERE column3 = 'value'"
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)
