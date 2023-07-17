import ply.yacc as yacc
from lex import tokens


def p_print_statement(p):
    '''
    print_statement : PRINT ID LPAREN num_strimg_statement RPAREN
    '''
    p[0] =  (p[1], p[2], p[3], p[4], p[5])

def p_num_strimg_statement(p):
    '''
    num_strimg_statement : NUMBER
                         | num_strimg_statement COMMA NUMBER
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_error(p):
    if p:
        print("Error de sintaxis en la entrada en la posición", p)
    else:
        print("Error de sintaxis en la entrada")

parser = yacc.yacc()

# Prueba del analizador sintáctico
result = parser.parse("PRINT asdasd(23, 34,34, 34, 34,4, 6,7)")
print(result)