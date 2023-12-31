class Palabras_Reservadas:

    def __init(self):
        # Palabras Reservadas
        self.mReservadas = {
            "SELECT": "select",
            "INSERT": "insert",
            "UPDATE": "update",
            "DELETE": "delete",
            "FROM": "from",
            "WHERE": "where",
            "AND": " and",
            "OR": "or",
            "NOT": "not",
            "JOIN": "join",
            "INNER JOIN": "inner join",
            "LEFT JOIN": "left join",
            "RIGHT JOIN": "right join", 
            "OUTER JOIN": "outer join", 
            "ON": "on", 
            "GROUP BY": "group by", 
            "ORDER BY": "oder by", 
            "ASC": "asc", 
            "DESC": "desc", 
            "HAVING": "having", 
            "AS": "as", 
            "DISTINCT": "distinct", 
            "TOP": "top", 
            "LIMIT": "limit", 
            "OFFSET": "offset", 
            "UNION": "union", 
            "CREATE": "create", 
            "ALTER": "alter", 
            "DROP": "drop", 
            "TRUNCATE": "truncate", 
            "TABLE": "table", 
            "INDEX": "index", 
            "CONSTRAINT": "constraint", 
            "PRIMARY KEY": "primary key", 
            "FOREIGN KEY": "foreingn key", 
            "REFERENCES": "references", 
            "UNIQUE": "unique", 
            "CHECK": "check", 
            "DEFAULT": "default", 
            "NULL": "null", 
            "BETWEEN": "between", 
            "IN": "in", 
            "LIKE": "like", 
            "EXISTS": "exists", 
            "ANY": "any", 
            "ALL": "all", 
            "CASE": "case", 
            "WHEN": "when", 
            "THEN": "then", 
            "ELSE": "else", 
            "END": "end", 
            "CAST": "cast", 
            "CONVERT": "convert", 
            "AVG": "avg", 
            "SUM": "sum", 
            "COUNT": "count", 
            "MAX": "max", 
            "MIN": "min"
        }

        self.Reservadas = {

            "PROGRAMA" : "programa",
            "SI" : "si",
            "ENTONCES" : "entonces",
            "OTRO" : "otro",
            "HAZ" : "haz",
            "MIENTRAS" : "mientras",
            "COMIENZA" : "comienza",
            "TERMINA" : "termina",
            "IMPRIME" : "imprime",
            "REPITE" : "repite",
            "HASTA" : "hasta",
            "PARA" : "para",
            "A" : "a"

        }

        # Tokens lexicograficos
        self.HECHO = "FIN DE ARCHIVO"
        self.EOS = "EOS"
        self.COMENTARIO = "COMENTARIO"
        self.P_RES = "PALABRA RESERVADA"
        self.CADENA = "CADENA"
        self.RELOP = "OPE. RELACIONAL"
        self.LOGOP = "OPE. LOGICO"
        self.ADDOP = "OPE. DE SUMA O RESTA"
        self.MULOP = "OPE. DE MULTIPLACION O DIVISION"
        self.MODULO = "OPE. DE MODULO"
        self.STRINGS = "CADENAS DE CARACTERES"
        self.ERROR = "ERROR LEXICOGRAFICO"
        self.ERROR_SINTACTICO = "ERROR SINTACTICO"
        self.TOKEN_INV = "TOKEN INVALIDO"
        self.RESTO_MUNDO = "RESTO DEL MUNDO"
        self.ASIGNACION = "ASIGNACION"
        self.ID = "IDENTIFICADOR"
        self.NUM_ENT = "ENTERO"
        self.DELIMITADOR = "DELIMITADOR"

        # Palabras reservadas para el generaor de codigo intermedio

        self.VALOR_I = "lvalue"
        self.VALOR_D = "rvalue"
        self.PUSH = "push"
        self.ASING = ":="
        self.ETIQUETA = "label"
        self.VE_A =  "goto"
        self.SI_FALSO_VE_A = "gofalse"
        self.ESCRIBE = "write"
        self.COPIA = "print"
        self.HALT = "halt"


        self.PC = ";"
        self.IGUAL = "="
        self.PTSSA="("
        self.PTSSC=")"