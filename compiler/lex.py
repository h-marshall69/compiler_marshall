import ply.lex as lex

# Lista de palabras clave en SQL
keywords = {
    'SELECT': 'SELECT',
    'FROM': 'FROM',
    'WHERE': 'WHERE',
    'AND': 'AND',
    'OR': 'OR',
    'NOT': 'NOT',
    'INSERT': 'INSERT',
    'INTO': 'INTO',
    'VALUES': 'VALUES',
    'UPDATE': 'UPDATE',
    'SET': 'SET',
    'DELETE': 'DELETE',
    'CREATE': 'CREATE',
    'TABLE': 'TABLE',
    'DROP': 'DROP',
    'ALTER': 'ALTER',
    'ADD': 'ADD',
    'COLUMN': 'COLUMN',
    'PRIMARY': 'PRIMARY',
    'KEY': 'KEY',
    'FOREIGN': 'FOREIGN',
    'REFERENCES': 'REFERENCES',
    'INNER': 'INNER',
    'JOIN': 'JOIN',
    'LEFT': 'LEFT',
    'RIGHT': 'RIGHT',
    'FULL': 'FULL',
    'OUTER': 'OUTER',
    'ON': 'ON',
    'GROUP': 'GROUP',
    'BY': 'BY',
    'HAVING': 'HAVING',
    'ORDER': 'ORDER',
    'ASC': 'ASC',
    'DESC': 'DESC',
    'LIMIT': 'LIMIT',
}

# Lista de tokens
tokens = list(keywords.values()) + [
    'ID',         # Identificadores (nombres de tablas, columnas, etc.)
    'NUMBER',     # Números enteros
    'FLOAT',      # Números de punto flotante
    'STRING',     # Cadenas de texto entre comillas simples
    'LPAREN',     # Paréntesis izquierdo
    'RPAREN',     # Paréntesis derecho
    'COMMA',      # Coma
    'SEMICOLON',  # Punto y coma
    'EQ',         # Operador de igualdad (=)
    'NEQ',        # Operador de desigualdad (!= o <>)
    'LE',         # Operador de menor o igual que (<=)
    'GE',         # Operador de mayor o igual que (>=)
    'LT',         # Operador de menor que (<)
    'GT',         # Operador de mayor que (>)
]

# Expresiones regulares para tokens simples
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'
t_EQ = r'='
t_NEQ = r'(!=|<>)'
t_LE = r'<='
t_GE = r'>='
t_LT = r'<'
t_GT = r'>'

# Expresiones regulares con acciones para tokens más complejos
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value.upper(), 'ID')
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\'[^\']*\''
    t.value = t.value[1:-1]  # Eliminar comillas simples alrededor de la cadena
    return t

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'

# Manejo de saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de comentarios
def t_COMMENT(t):
    r'--.*'
    pass  # Los comentarios no generan tokens, simplemente se ignoran

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lexer.lineno}")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Prueba del analizador léxico con una sentencia SQL
data = """
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;
"""

#lexer.input(data)

#while True:
#    tok = lexer.token()
#    if not tok:
#        break  # Se han procesado todos los tokens
#    print(tok)
