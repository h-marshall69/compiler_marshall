import ply.yacc as yacc
from compiler.lex import tokens

# Reglas de la gramática
def p_statement(p):
    '''
    statement : select_statement
    '''
    print('SELECT statement recognized')

def p_select_statement(p):
    '''
    select_statement : SELECT FROM
    '''
    print('SELECT statement recognized')


def p_error(p):
    print(f'Syntax error at {p.value}')


# Construcción del parser
#parser = yacc.yacc()

# Prueba de la gramática con una sentencia SELECT
#data = 'SELECT FROM'
#parser.parse(data)