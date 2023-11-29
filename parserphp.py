import ply.yacc as sint

from main import tokens

resultado_sintactico = []

def p_sentencias(p):
    '''sentencias : asignacion'''

def p_valores(p):
  '''valores : valor
            | valor COMMA valores'''

def p_numero(p):
  '''NUMERO : ENTERO
            | FLOTANTE
  '''
def p_valor(p):
    '''valor : NUMERO
	         | CADENA
	         | BOOLEAN
           | IDENTIFICADOR
	'''
def p_echo(p):
  '''ECHO : ECHO valores PUNTOCOMA
  '''
def p_operadores(p):
   '''operadores : OPERADOR
	         | AND
	         | OR
	'''


# Asignacion
def p_asignacion(p):
    '''asignacion : IDENTIFICADOR ASIGNAR valor'''

# Impresion
def p_print(p):
  '''print : PRINT PARENIZ valores PARENDER PUNTOCOMA
        | PRINT valor PUNTOCOMA'''

def p_print_sinvalor(p):
  "print : PRINT PARENIZ PARENDER PUNTOCOMA"

def p_printf_conformato(p):
  "printf : PRINTF PARENIZ valores PARENDER PUNTOCOMA"

# Operaciones aritmeticas

def p_operadorAritmetico(p):
    '''operadorAritmetico : SUMA
						  | RESTA
						  | MULT
						  | DIVISION
              | DIVISIONENTERA
						  | MODULO
						  | POTENCIA
	'''

