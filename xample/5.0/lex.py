import ply.lex as lex

# List of token names.   This is always required
tokens = [
    'COMMENT',
    'FLOAT',
    'NUMBER',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUAL',
    'COMMA',
    'ID',
]


    
# Regular expression rules for simple tokens
t_PLUS          = r'\+'
t_MINUS         = r'-'
t_TIMES         = r'\*'
t_DIVIDE        = r'/'
t_LPAREN        = r'\('
t_RPAREN        = r'\)'
t_EQUAL         = r'\='
t_COMMA         = r','



def t_COMMENT(t):
    r'\#.*'
    pass

# A regular expression rule with some action code
def t_FLOAT(t):
	r'[\d]+[.][\d]+'
	t.value = float(t.value)
	return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# A regular expression for detecting the string in double codes
def t_STRING(t):
	r'(\")[a-zA-Z]+[a-zA-Z0-9]*(\")'
	t.value = str(t.value)
	return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

reserved = [
    'IF',
    'THEN',
    'ELSE',
    'WHILE',
    'WHERE',
    'BIGINT',
    'CREATE',
    'INSERT',
    'TABLE',
    'SELECT',
    'DELETE',
    'FOR',
    'PRINT'
]

tokens = tokens + reserved

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reserved:
        t.value = t.value.upper()
        t.type = t.value
        return t
    
    return t

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
    INSERTd xm.insert(23.0)
'''

# Give the lexer some input
lexer.input(data)


# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
