import ply.yacc as sint

from main import tokens

resultado_sintactico = []

def p_sentencias(p):
    '''sentencias : asignacion
                  | echo 
                  | funcion
                  | print
                  | operadorAritmetico
                  | return 
                  | estructuras
                  | estructurasControl
                  '''

def p_valores(p):
  '''valores : valor
            | valor COMA valores'''

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
def p_comparadorNum(p):
	''' comparadorNum : MAYORQUE
					| MAYORIGUALQUE
					| MENORQUE
					| MENORIGUALQUE
	'''
def p_comparador(p):
	''' comparador : IDENTICO
					| NOIDENTICO
					| IGUAL
	'''
    
def p_variableOperacion(p):
    ''' variables : NUMERO
                  | IDENTIFICADOR
    '''

def p_comparaciones(p):
	''' comparaciones : comparacion  
					 | comparacion operadores comparaciones
	'''

def p_comparacion(p):
	''' comparacion :  variables comparadorNum variables 
            | valor comparador valor 
	'''

def p_incrementoDecremento(p):
  '''incrementoDecremento : INCREMENTO
                          | DECREMENTO
                          | SUMA ENTERO
                          | RESTA ENTERO
  '''

# FALTA ARGUMENTOOOOOOS
def p_while(p):
	''' while : WHILE PARENIZ comparaciones PARENDER LLAVEIZ 
	'''

def p_for(p):
  ''' for : FOR PARENIZ IDENTIFICADOR ASIGNAR ENTERO PUNTOCOMA IDENTIFICADOR comparadorNum ENTERO PUNTOCOMA IDENTIFICADOR incrementoDecremento PARENDER LLAVEIZ
  '''
#for ($i = 2; $i <= 10; $i + 2) {

def p_if(p):
  ''' if : IF PARENIZ comparaciones PARENDER LLAVEIZ
          | IF PARENIZ IDENTIFICADOR PARENDER LLAVEIZ 
  '''
#if ($edad >= 18) {
#if ($esAdmin) { 

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

def p_echo(p):
  '''echo : ECHO valores PUNTOCOMA
  '''

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
    "funcion : FUNCTION NAMEFUNCTION PARENIZ parametro PARENDER LLAVEIZ"
# function sumar($numero1, $numero2) {


#Declaracion de un parametro
def p_parametro(p):
   '''parametro : IDENTIFICADOR
                | IDENTIFICADOR COMA parametro
'''

#llamada a una funcion
def p_llamada_funcion(p):
    ''' funcion : NAMEFUNCTION PARENIZ parametro PARENDER PUNTOCOMA
                | IDENTIFICADOR ASIGNAR NAMEFUNCTION PARENIZ parametro PARENDER PUNTOCOMA
'''

# return 
def p_return(p):
  " return : RETURN IDENTIFICADOR PUNTOCOMA"
#return $resultado;

# sumar($valor1, $valor2);
# $suma = sumar($valor1, $valor2);

#ESTRUCTURA DE DATOS
#QUEUE

# $queue = new SplQueue(); 
def p_estructuras(p):
  '''estructuras : queue
                  | stack
                  | array
                  '''

def p_estructurasControl(p):
  '''estructurasControl : while
                        | for
                        | if
  '''

def p_queue(p):
  " queue : IDENTIFICADOR ASIGNAR NEW QUEUE PARENIZ PARENDER PUNTOCOMA"  

def p_stack(p):
  ''' stack : IDENTIFICADOR FLECHASIMPLE PUSH PARENIZ valor PARENDER PUNTOCOMA'''

#ARRAY
def p_array(p):
  ''' array : IDENTIFICADOR ASIGNAR ARRAY PARENIZ valores PARENDER PUNTOCOMA
            | IDENTIFICADOR ASIGNAR CORCHETEIZ valores CORCHETEDER PUNTOCOMA
  '''
#$arrayNumerico = array(1, 2, 3, 4, 5);
#$arrayNumerico = [1, 2, 3, 4, 5];

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