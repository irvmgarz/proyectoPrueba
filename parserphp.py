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
def p_comparacionNum(p):
	''' comparacion : MAYORQUE
					| MAYORIGUALQUE
					| MENORQUE
					| MENORIGUALQUE
					| IDENTICO
					| NOIDENTICO
					| IGUAL
	'''
def p_comparaciones(p):
	''' comparaciones : valor comparacion valor
	'''
def p_echo(p):
  '''ECHO : ECHO valores PUNTOCOMA
  '''
def p_while(p):
	''' WHILE : WHILE 
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

#Inicio Diego Martinez

#FUNCIONES
#declaracion de una funcion
def p_declaracion_funcion(p):
    "funcion : FUNCTION NAMEFUNCTION PARENIZ parametro PARENDER LLAVEIZQ"
# function sumar($numero1, $numero2) {


#Declaracion de un parametro
def p_parametro(p):
   '''parametro : IDENTIFICADOR
                | IDENTIFICADOR COMA parametro
'''

#llamada a una funcion
def p_llamada_funcion(p):
    ''' funcion : NAMEFUNCTION PARENIZ parametro PARENDER PUNTOYCOMA
                | IDENTIFICADOR ASIGNAR NAMEFUNCTION PARENIZ parametro PARENDER SEMICOLON
'''

# return 
def p_return(p):
  " return : RETURN IDENTIFICADOR PUNTOYCOMA"
#return $resultado;

# sumar($valor1, $valor2);
# $suma = sumar($valor1, $valor2);
                
#Fin de Diego Martinez

def p_error(p):
    try:
        if p:
            print(f"Error de sintaxis en la línea {p.lineno}, posición {p.lexpos}: Token inesperado '{p.value}'")
        else:
            print("Error de sintaxis: entrada inesperada al final del archivo")
    except Exception as e:
        # Manejar cualquier excepción no esperada y mostrar un mensaje genérico
        print(f"Error inesperado: {str(e)}")


# Build the parser
parser = sint.yacc()

while True:
  try:
    s = input('prueba > ')
    #s = code_meiyin
  except EOFError:
    break
  if not s: continue
  result = parser.parse(s)
  print(result)