
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ANDEQUAL ARRAY AS ASIGNACION ASIGNAR BOOLEAN BREAK CADENA CASE COMA COMENTARIO CORCHETEDER CORCHETEIZ COUNT CURRENT DECREMENTO DEFAULT DEQUEUE DIVISION DIVISIONENTERA DOSPUNTOS ECHO ELSE ELSEIF ENQUEUE ENTERO FLECHASIMPLE FLOTANTE FOR FOREACH FUNCTION IDENTICO IDENTIFICADOR IF IGUAL INCREMENTO LLAVEDER LLAVEIZ MAYORIGUALQUE MAYORQUE MENORIGUALQUE MENORQUE MODULO MULT NAMEFUNCTION NEW NEXT NOIDENTICO OPERADOR OR PARENDER PARENIZ POP POTENCIA PRINT PUNTO PUNTOCOMA PUSH QUEUE RESTA RETURN REWIND SIGNOID STACK SUMA SWITCH VALID WHILEsentencias : asignacion\n                  | echo \n                  | funcion\n                  | print\n                  | operadorAritmetico\n                  | return \n                  | estructuras\n                  | estructurasControl\n                  valores : valor\n            | valor COMA valoresNUMERO : ENTERO\n            | FLOTANTE\n  valor : NUMERO\n\t         | CADENA\n\t         | BOOLEAN\n             | IDENTIFICADOR\n\t comparadorNum : MAYORQUE\n\t\t\t\t\t| MAYORIGUALQUE\n\t\t\t\t\t| MENORQUE\n\t\t\t\t\t| MENORIGUALQUE\n\t comparador : IDENTICO\n\t\t\t\t\t| NOIDENTICO\n\t\t\t\t\t| IGUAL\n\t variables : NUMERO\n                  | IDENTIFICADOR\n     comparaciones : comparacion  \n\t\t\t\t\t | comparacion operadores comparaciones\n\t comparacion :  variables comparadorNum variables \n            | valor comparador valor \n\tincrementoDecremento : INCREMENTO\n                          | DECREMENTO\n                          | SUMA ENTERO\n                          | RESTA ENTERO\n   while : WHILE PARENIZ comparaciones PARENDER LLAVEIZ \n\t for : FOR PARENIZ IDENTIFICADOR ASIGNAR ENTERO PUNTOCOMA IDENTIFICADOR comparadorNum ENTERO PUNTOCOMA IDENTIFICADOR incrementoDecremento PARENDER LLAVEIZ\n   foreach : FOREACH PARENIZ IDENTIFICADOR AS IDENTIFICADOR PARENDER LLAVEIZ casos : caso \n             | caso casos\n   caso : CASE valor DOSPUNTOS echo BREAK PUNTOCOMA\n   switch : SWITCH PARENIZ valor PARENDER LLAVEIZ casos DEFAULT DOSPUNTOS echo LLAVEDER\n   if : IF PARENIZ comparaciones PARENDER LLAVEIZ\n          | IF PARENIZ IDENTIFICADOR PARENDER LLAVEIZ \n  operadores : OPERADOR\n\t         | AND\n\t         | OR\n\tasignacion : IDENTIFICADOR ASIGNAR valor PUNTOCOMAprint : PRINT PARENIZ valores PARENDER PUNTOCOMA\n        | PRINT valor PUNTOCOMAprint : PRINT PARENIZ PARENDER PUNTOCOMAecho : ECHO valores PUNTOCOMA\n  operadorAritmetico : SUMA\n\t\t\t\t\t\t  | RESTA\n\t\t\t\t\t\t  | MULT\n\t\t\t\t\t\t  | DIVISION\n              | DIVISIONENTERA\n\t\t\t\t\t\t  | MODULO\n\t\t\t\t\t\t  | POTENCIA\n\tfuncion : FUNCTION NAMEFUNCTION PARENIZ parametro PARENDER LLAVEIZparametro : IDENTIFICADOR\n                | IDENTIFICADOR COMA parametro\n funcion : NAMEFUNCTION PARENIZ parametro PARENDER PUNTOCOMA\n                | IDENTIFICADOR ASIGNAR NAMEFUNCTION PARENIZ parametro PARENDER PUNTOCOMA\n return : RETURN IDENTIFICADOR PUNTOCOMAestructuras : queue\n                  | stack\n                  | array\n                  estructurasControl : while\n                        | for\n                        | if\n                        | foreach\n                        | switch\n   queue : IDENTIFICADOR ASIGNAR NEW QUEUE PARENIZ PARENDER PUNTOCOMA queue : IDENTIFICADOR FLECHASIMPLE ENQUEUE PARENIZ valor PARENDER PUNTOCOMA queue : IDENTIFICADOR FLECHASIMPLE COUNT PARENIZ PARENDER PUNTOCOMA queue : IDENTIFICADOR FLECHASIMPLE DEQUEUE PARENIZ PARENDER PUNTOCOMA queue : IDENTIFICADOR FLECHASIMPLE NEXT PARENIZ PARENDER PUNTOCOMA queue : IDENTIFICADOR FLECHASIMPLE REWIND PARENIZ PARENDER PUNTOCOMA queue : IDENTIFICADOR FLECHASIMPLE CURRENT PARENIZ PARENDER PUNTOCOMA queue : IDENTIFICADOR FLECHASIMPLE VALID PARENIZ PARENDER stack : IDENTIFICADOR FLECHASIMPLE PUSH PARENIZ valor PARENDER PUNTOCOMA stack : IDENTIFICADOR ASIGNAR NEW STACK PARENIZ PARENDER PUNTOCOMA stack : IDENTIFICADOR FLECHASIMPLE NEXT PARENIZ PARENDER PUNTOCOMA stack : IDENTIFICADOR FLECHASIMPLE REWIND PARENIZ PARENDER PUNTOCOMA stack : IDENTIFICADOR FLECHASIMPLE CURRENT PARENIZ PARENDER PUNTOCOMA stack : IDENTIFICADOR FLECHASIMPLE VALID PARENIZ PARENDER array : IDENTIFICADOR ASIGNAR ARRAY PARENIZ valores PARENDER PUNTOCOMA\n            | IDENTIFICADOR ASIGNAR CORCHETEIZ valores CORCHETEDER PUNTOCOMA\n  '
    
_lr_action_items = {'IDENTIFICADOR':([0,11,14,22,36,47,48,51,52,53,54,55,60,70,71,90,93,95,102,106,110,111,112,113,114,115,116,117,118,119,120,121,122,126,169,173,191,],[10,43,43,50,43,73,43,83,84,86,87,43,43,43,73,73,43,43,43,73,83,-43,-44,-45,149,-17,-18,-19,-20,43,-21,-22,-23,154,180,43,194,]),'ECHO':([0,186,187,],[11,11,11,]),'FUNCTION':([0,],[12,]),'NAMEFUNCTION':([0,12,36,],[13,46,57,]),'PRINT':([0,],[14,]),'SUMA':([0,194,],[15,199,]),'RESTA':([0,194,],[16,200,]),'MULT':([0,],[17,]),'DIVISION':([0,],[18,]),'DIVISIONENTERA':([0,],[19,]),'MODULO':([0,],[20,]),'POTENCIA':([0,],[21,]),'RETURN':([0,],[22,]),'WHILE':([0,],[31,]),'FOR':([0,],[32,]),'IF':([0,],[33,]),'FOREACH':([0,],[34,]),'SWITCH':([0,],[35,]),'$end':([1,2,3,4,5,6,7,8,9,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,69,76,77,89,108,139,142,144,145,152,153,160,162,163,164,165,166,168,174,175,176,177,178,179,181,192,204,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-51,-52,-53,-54,-55,-56,-57,-64,-65,-66,-67,-68,-69,-70,-71,-50,-48,-63,-46,-49,-79,-61,-47,-34,-41,-42,-87,-74,-75,-76,-77,-78,-58,-62,-72,-81,-86,-73,-80,-36,-40,-35,]),'ASIGNAR':([10,84,],[36,123,]),'FLECHASIMPLE':([10,],[37,]),'CADENA':([11,14,36,48,51,53,55,60,70,93,95,102,110,111,112,113,119,120,121,122,173,],[41,41,41,41,41,41,41,41,41,41,41,41,41,-43,-44,-45,41,-21,-22,-23,41,]),'BOOLEAN':([11,14,36,48,51,53,55,60,70,93,95,102,110,111,112,113,119,120,121,122,173,],[42,42,42,42,42,42,42,42,42,42,42,42,42,-43,-44,-45,42,-21,-22,-23,42,]),'ENTERO':([11,14,36,48,51,53,55,60,70,93,95,102,110,111,112,113,114,115,116,117,118,119,120,121,122,123,173,185,199,200,],[44,44,44,44,44,44,44,44,44,44,44,44,44,-43,-44,-45,44,-17,-18,-19,-20,44,-21,-22,-23,151,44,188,202,203,]),'FLOTANTE':([11,14,36,48,51,53,55,60,70,93,95,102,110,111,112,113,114,115,116,117,118,119,120,121,122,173,],[45,45,45,45,45,45,45,45,45,45,45,45,45,-43,-44,-45,45,-17,-18,-19,-20,45,-21,-22,-23,45,]),'PARENIZ':([13,14,31,32,33,34,35,46,57,59,61,62,63,64,65,66,67,68,91,92,],[47,48,51,52,53,54,55,71,90,93,95,96,97,98,99,100,101,102,129,130,]),'NEW':([36,],[58,]),'ARRAY':([36,],[59,]),'CORCHETEIZ':([36,],[60,]),'ENQUEUE':([37,],[61,]),'COUNT':([37,],[62,]),'DEQUEUE':([37,],[63,]),'NEXT':([37,],[64,]),'REWIND':([37,],[65,]),'CURRENT':([37,],[66,]),'VALID':([37,],[67,]),'PUSH':([37,],[68,]),'PUNTOCOMA':([38,39,40,41,42,43,44,45,49,50,56,75,103,105,107,132,134,135,136,137,138,151,156,157,158,159,161,167,188,193,],[69,-9,-13,-14,-15,-16,-11,-12,76,77,89,108,-10,142,144,160,162,163,164,165,166,169,174,175,176,177,178,179,191,195,]),'PARENDER':([39,40,41,42,43,44,45,48,72,73,74,78,79,85,86,88,96,97,98,99,100,101,103,104,128,129,130,131,133,140,143,146,147,148,149,150,154,196,197,198,202,203,],[-9,-13,-14,-15,-16,-11,-12,75,105,-59,107,109,-26,124,125,127,134,135,136,137,138,139,-10,141,156,157,158,159,161,167,-60,-27,-28,-24,-25,-29,170,201,-30,-31,-32,-33,]),'CORCHETEDER':([39,40,41,42,43,44,45,94,103,],[-9,-13,-14,-15,-16,-11,-12,132,-10,]),'COMA':([39,40,41,42,43,44,45,73,],[70,-13,-14,-15,-16,-11,-12,106,]),'OPERADOR':([40,41,42,43,44,45,79,147,148,149,150,],[-13,-14,-15,-16,-11,-12,111,-28,-24,-25,-29,]),'AND':([40,41,42,43,44,45,79,147,148,149,150,],[-13,-14,-15,-16,-11,-12,112,-28,-24,-25,-29,]),'OR':([40,41,42,43,44,45,79,147,148,149,150,],[-13,-14,-15,-16,-11,-12,113,-28,-24,-25,-29,]),'DOSPUNTOS':([40,41,42,43,44,45,182,184,],[-13,-14,-15,-16,-11,-12,186,187,]),'IDENTICO':([41,42,44,45,81,82,83,86,],[-14,-15,-11,-12,120,-13,-16,-16,]),'NOIDENTICO':([41,42,44,45,81,82,83,86,],[-14,-15,-11,-12,121,-13,-16,-16,]),'IGUAL':([41,42,44,45,81,82,83,86,],[-14,-15,-11,-12,122,-13,-16,-16,]),'MAYORQUE':([44,45,80,82,83,86,180,],[-11,-12,115,-24,-25,-25,115,]),'MAYORIGUALQUE':([44,45,80,82,83,86,180,],[-11,-12,116,-24,-25,-25,116,]),'MENORQUE':([44,45,80,82,83,86,180,],[-11,-12,117,-24,-25,-25,117,]),'MENORIGUALQUE':([44,45,80,82,83,86,180,],[-11,-12,118,-24,-25,-25,118,]),'QUEUE':([58,],[91,]),'STACK':([58,],[92,]),'LLAVEDER':([69,189,],[-50,192,]),'BREAK':([69,190,],[-50,193,]),'AS':([87,],[126,]),'LLAVEIZ':([109,124,125,127,141,170,201,],[145,152,153,155,168,181,204,]),'CASE':([155,172,195,],[173,173,-39,]),'DEFAULT':([171,172,183,195,],[182,-37,-38,-39,]),'INCREMENTO':([194,],[197,]),'DECREMENTO':([194,],[198,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencias':([0,],[1,]),'asignacion':([0,],[2,]),'echo':([0,186,187,],[3,189,190,]),'funcion':([0,],[4,]),'print':([0,],[5,]),'operadorAritmetico':([0,],[6,]),'return':([0,],[7,]),'estructuras':([0,],[8,]),'estructurasControl':([0,],[9,]),'queue':([0,],[23,]),'stack':([0,],[24,]),'array':([0,],[25,]),'while':([0,],[26,]),'for':([0,],[27,]),'if':([0,],[28,]),'foreach':([0,],[29,]),'switch':([0,],[30,]),'valores':([11,48,60,70,93,],[38,74,94,103,131,]),'valor':([11,14,36,48,51,53,55,60,70,93,95,102,110,119,173,],[39,49,56,39,81,81,88,39,39,39,133,140,81,150,184,]),'NUMERO':([11,14,36,48,51,53,55,60,70,93,95,102,110,114,119,173,],[40,40,40,40,82,82,40,40,40,40,40,40,82,148,40,40,]),'parametro':([47,71,90,106,],[72,104,128,143,]),'comparaciones':([51,53,110,],[78,85,146,]),'comparacion':([51,53,110,],[79,79,79,]),'variables':([51,53,110,114,],[80,80,80,147,]),'operadores':([79,],[110,]),'comparadorNum':([80,180,],[114,185,]),'comparador':([81,],[119,]),'casos':([155,172,],[171,183,]),'caso':([155,172,],[172,172,]),'incrementoDecremento':([194,],[196,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencias","S'",1,None,None,None),
  ('sentencias -> asignacion','sentencias',1,'p_sentencias','parserphp.py',8),
  ('sentencias -> echo','sentencias',1,'p_sentencias','parserphp.py',9),
  ('sentencias -> funcion','sentencias',1,'p_sentencias','parserphp.py',10),
  ('sentencias -> print','sentencias',1,'p_sentencias','parserphp.py',11),
  ('sentencias -> operadorAritmetico','sentencias',1,'p_sentencias','parserphp.py',12),
  ('sentencias -> return','sentencias',1,'p_sentencias','parserphp.py',13),
  ('sentencias -> estructuras','sentencias',1,'p_sentencias','parserphp.py',14),
  ('sentencias -> estructurasControl','sentencias',1,'p_sentencias','parserphp.py',15),
  ('valores -> valor','valores',1,'p_valores','parserphp.py',19),
  ('valores -> valor COMA valores','valores',3,'p_valores','parserphp.py',20),
  ('NUMERO -> ENTERO','NUMERO',1,'p_numero','parserphp.py',23),
  ('NUMERO -> FLOTANTE','NUMERO',1,'p_numero','parserphp.py',24),
  ('valor -> NUMERO','valor',1,'p_valor','parserphp.py',27),
  ('valor -> CADENA','valor',1,'p_valor','parserphp.py',28),
  ('valor -> BOOLEAN','valor',1,'p_valor','parserphp.py',29),
  ('valor -> IDENTIFICADOR','valor',1,'p_valor','parserphp.py',30),
  ('comparadorNum -> MAYORQUE','comparadorNum',1,'p_comparadorNum','parserphp.py',33),
  ('comparadorNum -> MAYORIGUALQUE','comparadorNum',1,'p_comparadorNum','parserphp.py',34),
  ('comparadorNum -> MENORQUE','comparadorNum',1,'p_comparadorNum','parserphp.py',35),
  ('comparadorNum -> MENORIGUALQUE','comparadorNum',1,'p_comparadorNum','parserphp.py',36),
  ('comparador -> IDENTICO','comparador',1,'p_comparador','parserphp.py',39),
  ('comparador -> NOIDENTICO','comparador',1,'p_comparador','parserphp.py',40),
  ('comparador -> IGUAL','comparador',1,'p_comparador','parserphp.py',41),
  ('variables -> NUMERO','variables',1,'p_variableOperacion','parserphp.py',45),
  ('variables -> IDENTIFICADOR','variables',1,'p_variableOperacion','parserphp.py',46),
  ('comparaciones -> comparacion','comparaciones',1,'p_comparaciones','parserphp.py',50),
  ('comparaciones -> comparacion operadores comparaciones','comparaciones',3,'p_comparaciones','parserphp.py',51),
  ('comparacion -> variables comparadorNum variables','comparacion',3,'p_comparacion','parserphp.py',55),
  ('comparacion -> valor comparador valor','comparacion',3,'p_comparacion','parserphp.py',56),
  ('incrementoDecremento -> INCREMENTO','incrementoDecremento',1,'p_incrementoDecremento','parserphp.py',60),
  ('incrementoDecremento -> DECREMENTO','incrementoDecremento',1,'p_incrementoDecremento','parserphp.py',61),
  ('incrementoDecremento -> SUMA ENTERO','incrementoDecremento',2,'p_incrementoDecremento','parserphp.py',62),
  ('incrementoDecremento -> RESTA ENTERO','incrementoDecremento',2,'p_incrementoDecremento','parserphp.py',63),
  ('while -> WHILE PARENIZ comparaciones PARENDER LLAVEIZ','while',5,'p_while','parserphp.py',68),
  ('for -> FOR PARENIZ IDENTIFICADOR ASIGNAR ENTERO PUNTOCOMA IDENTIFICADOR comparadorNum ENTERO PUNTOCOMA IDENTIFICADOR incrementoDecremento PARENDER LLAVEIZ','for',14,'p_for','parserphp.py',72),
  ('foreach -> FOREACH PARENIZ IDENTIFICADOR AS IDENTIFICADOR PARENDER LLAVEIZ','foreach',7,'p_foreach','parserphp.py',78),
  ('casos -> caso','casos',1,'p_casos','parserphp.py',82),
  ('casos -> caso casos','casos',2,'p_casos','parserphp.py',83),
  ('caso -> CASE valor DOSPUNTOS echo BREAK PUNTOCOMA','caso',6,'p_caso','parserphp.py',87),
  ('switch -> SWITCH PARENIZ valor PARENDER LLAVEIZ casos DEFAULT DOSPUNTOS echo LLAVEDER','switch',10,'p_switch','parserphp.py',91),
  ('if -> IF PARENIZ comparaciones PARENDER LLAVEIZ','if',5,'p_if','parserphp.py',95),
  ('if -> IF PARENIZ IDENTIFICADOR PARENDER LLAVEIZ','if',5,'p_if','parserphp.py',96),
  ('operadores -> OPERADOR','operadores',1,'p_operadores','parserphp.py',102),
  ('operadores -> AND','operadores',1,'p_operadores','parserphp.py',103),
  ('operadores -> OR','operadores',1,'p_operadores','parserphp.py',104),
  ('asignacion -> IDENTIFICADOR ASIGNAR valor PUNTOCOMA','asignacion',4,'p_asignacion','parserphp.py',110),
  ('print -> PRINT PARENIZ valores PARENDER PUNTOCOMA','print',5,'p_print','parserphp.py',115),
  ('print -> PRINT valor PUNTOCOMA','print',3,'p_print','parserphp.py',116),
  ('print -> PRINT PARENIZ PARENDER PUNTOCOMA','print',4,'p_print_sinvalor','parserphp.py',119),
  ('echo -> ECHO valores PUNTOCOMA','echo',3,'p_echo','parserphp.py',122),
  ('operadorAritmetico -> SUMA','operadorAritmetico',1,'p_operadorAritmetico','parserphp.py',128),
  ('operadorAritmetico -> RESTA','operadorAritmetico',1,'p_operadorAritmetico','parserphp.py',129),
  ('operadorAritmetico -> MULT','operadorAritmetico',1,'p_operadorAritmetico','parserphp.py',130),
  ('operadorAritmetico -> DIVISION','operadorAritmetico',1,'p_operadorAritmetico','parserphp.py',131),
  ('operadorAritmetico -> DIVISIONENTERA','operadorAritmetico',1,'p_operadorAritmetico','parserphp.py',132),
  ('operadorAritmetico -> MODULO','operadorAritmetico',1,'p_operadorAritmetico','parserphp.py',133),
  ('operadorAritmetico -> POTENCIA','operadorAritmetico',1,'p_operadorAritmetico','parserphp.py',134),
  ('funcion -> FUNCTION NAMEFUNCTION PARENIZ parametro PARENDER LLAVEIZ','funcion',6,'p_declaracion_funcion','parserphp.py',145),
  ('parametro -> IDENTIFICADOR','parametro',1,'p_parametro','parserphp.py',151),
  ('parametro -> IDENTIFICADOR COMA parametro','parametro',3,'p_parametro','parserphp.py',152),
  ('funcion -> NAMEFUNCTION PARENIZ parametro PARENDER PUNTOCOMA','funcion',5,'p_llamada_funcion','parserphp.py',157),
  ('funcion -> IDENTIFICADOR ASIGNAR NAMEFUNCTION PARENIZ parametro PARENDER PUNTOCOMA','funcion',7,'p_llamada_funcion','parserphp.py',158),
  ('return -> RETURN IDENTIFICADOR PUNTOCOMA','return',3,'p_return','parserphp.py',163),
  ('estructuras -> queue','estructuras',1,'p_estructuras','parserphp.py',174),
  ('estructuras -> stack','estructuras',1,'p_estructuras','parserphp.py',175),
  ('estructuras -> array','estructuras',1,'p_estructuras','parserphp.py',176),
  ('estructurasControl -> while','estructurasControl',1,'p_estructurasControl','parserphp.py',180),
  ('estructurasControl -> for','estructurasControl',1,'p_estructurasControl','parserphp.py',181),
  ('estructurasControl -> if','estructurasControl',1,'p_estructurasControl','parserphp.py',182),
  ('estructurasControl -> foreach','estructurasControl',1,'p_estructurasControl','parserphp.py',183),
  ('estructurasControl -> switch','estructurasControl',1,'p_estructurasControl','parserphp.py',184),
  ('queue -> IDENTIFICADOR ASIGNAR NEW QUEUE PARENIZ PARENDER PUNTOCOMA','queue',7,'p_queue','parserphp.py',189),
  ('queue -> IDENTIFICADOR FLECHASIMPLE ENQUEUE PARENIZ valor PARENDER PUNTOCOMA','queue',7,'p_colaAnadir','parserphp.py',194),
  ('queue -> IDENTIFICADOR FLECHASIMPLE COUNT PARENIZ PARENDER PUNTOCOMA','queue',6,'p_colaContar','parserphp.py',199),
  ('queue -> IDENTIFICADOR FLECHASIMPLE DEQUEUE PARENIZ PARENDER PUNTOCOMA','queue',6,'p_colaExpulsar','parserphp.py',204),
  ('queue -> IDENTIFICADOR FLECHASIMPLE NEXT PARENIZ PARENDER PUNTOCOMA','queue',6,'p_colaSiguiente','parserphp.py',209),
  ('queue -> IDENTIFICADOR FLECHASIMPLE REWIND PARENIZ PARENDER PUNTOCOMA','queue',6,'p_colaPunteroPrincipio','parserphp.py',214),
  ('queue -> IDENTIFICADOR FLECHASIMPLE CURRENT PARENIZ PARENDER PUNTOCOMA','queue',6,'p_colaActual','parserphp.py',219),
  ('queue -> IDENTIFICADOR FLECHASIMPLE VALID PARENIZ PARENDER','queue',5,'p_colaValido','parserphp.py',224),
  ('stack -> IDENTIFICADOR FLECHASIMPLE PUSH PARENIZ valor PARENDER PUNTOCOMA','stack',7,'p_stackPush','parserphp.py',232),
  ('stack -> IDENTIFICADOR ASIGNAR NEW STACK PARENIZ PARENDER PUNTOCOMA','stack',7,'p_stack','parserphp.py',236),
  ('stack -> IDENTIFICADOR FLECHASIMPLE NEXT PARENIZ PARENDER PUNTOCOMA','stack',6,'p_stackAvanzar','parserphp.py',241),
  ('stack -> IDENTIFICADOR FLECHASIMPLE REWIND PARENIZ PARENDER PUNTOCOMA','stack',6,'p_stackPunteroPrincipio','parserphp.py',246),
  ('stack -> IDENTIFICADOR FLECHASIMPLE CURRENT PARENIZ PARENDER PUNTOCOMA','stack',6,'p_stackActual','parserphp.py',251),
  ('stack -> IDENTIFICADOR FLECHASIMPLE VALID PARENIZ PARENDER','stack',5,'p_stackValido','parserphp.py',256),
  ('array -> IDENTIFICADOR ASIGNAR ARRAY PARENIZ valores PARENDER PUNTOCOMA','array',7,'p_array','parserphp.py',263),
  ('array -> IDENTIFICADOR ASIGNAR CORCHETEIZ valores CORCHETEDER PUNTOCOMA','array',6,'p_array','parserphp.py',264),
]
