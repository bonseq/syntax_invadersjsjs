
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTIVO ALIANZA_EQUIPO ASIGNATURA BOOL CALLE CARGO CARRERA CIUDAD CLAVE_EMAIL CLAVE_LINK COMA CONCLUSION CORCHETE_DER CORCHETE_IZQ DIRECCION DOS_PUNTOS EDAD EMAIL ESTADO FECHA FECHA_FIN FECHA_INICIO FIRMA_DIGITAL FLOAT FOTO HABILIDADES IDENTIDAD_EQUIPO INTEGER INTEGRANTES LISTA_EQUIPOS LLAVE_DER LLAVE_IZQ NOMBRE NOMBRE_EQUIPO NULL PAIS PROYECTOS RESUMEN SALARIO STRING TAREAS UNIVERSIDAD_REGIONAL URL VERSION VIDEOjson : LLAVE_IZQ elementos LLAVE_DERelementos : par\n| elementos COMA parpar : clave DOS_PUNTOS valorclave : STRING\n| CLAVE_LINK\n| CLAVE_EMAIL\n| LISTA_EQUIPOS\n| NOMBRE_EQUIPO\n| IDENTIDAD_EQUIPO\n| ASIGNATURA\n| CARRERA\n| UNIVERSIDAD_REGIONAL\n| DIRECCION\n| ALIANZA_EQUIPO\n| INTEGRANTES\n| PROYECTOS\n| NOMBRE\n| EDAD\n| CARGO\n| FOTO\n| HABILIDADES\n| SALARIO\n| ACTIVO\n| ESTADO\n| RESUMEN\n| TAREAS\n| FECHA_INICIO\n| FECHA_FIN\n| VIDEO\n| CONCLUSION\n| CALLE\n| CIUDAD\n| PAIS\n| VERSION\n| FIRMA_DIGITAL\nobjeto : LLAVE_IZQ elementos LLAVE_DERlista : CORCHETE_IZQ valores CORCHETE_DERvalor : STRING\n| INTEGER\n| FLOAT\n| BOOL\n| NULL\n| FECHA\n| EMAIL\n| URL\n| objeto\n| listavalores : valor\n| valores COMA valor'
    
_lr_action_items = {'LLAVE_IZQ':([0,40,54,60,],[2,53,53,53,]),'$end':([1,38,],[0,-1,]),'STRING':([2,39,40,53,54,60,],[6,6,43,6,43,43,]),'CLAVE_LINK':([2,39,53,],[7,7,7,]),'CLAVE_EMAIL':([2,39,53,],[8,8,8,]),'LISTA_EQUIPOS':([2,39,53,],[9,9,9,]),'NOMBRE_EQUIPO':([2,39,53,],[10,10,10,]),'IDENTIDAD_EQUIPO':([2,39,53,],[11,11,11,]),'ASIGNATURA':([2,39,53,],[12,12,12,]),'CARRERA':([2,39,53,],[13,13,13,]),'UNIVERSIDAD_REGIONAL':([2,39,53,],[14,14,14,]),'DIRECCION':([2,39,53,],[15,15,15,]),'ALIANZA_EQUIPO':([2,39,53,],[16,16,16,]),'INTEGRANTES':([2,39,53,],[17,17,17,]),'PROYECTOS':([2,39,53,],[18,18,18,]),'NOMBRE':([2,39,53,],[19,19,19,]),'EDAD':([2,39,53,],[20,20,20,]),'CARGO':([2,39,53,],[21,21,21,]),'FOTO':([2,39,53,],[22,22,22,]),'HABILIDADES':([2,39,53,],[23,23,23,]),'SALARIO':([2,39,53,],[24,24,24,]),'ACTIVO':([2,39,53,],[25,25,25,]),'ESTADO':([2,39,53,],[26,26,26,]),'RESUMEN':([2,39,53,],[27,27,27,]),'TAREAS':([2,39,53,],[28,28,28,]),'FECHA_INICIO':([2,39,53,],[29,29,29,]),'FECHA_FIN':([2,39,53,],[30,30,30,]),'VIDEO':([2,39,53,],[31,31,31,]),'CONCLUSION':([2,39,53,],[32,32,32,]),'CALLE':([2,39,53,],[33,33,33,]),'CIUDAD':([2,39,53,],[34,34,34,]),'PAIS':([2,39,53,],[35,35,35,]),'VERSION':([2,39,53,],[36,36,36,]),'FIRMA_DIGITAL':([2,39,53,],[37,37,37,]),'LLAVE_DER':([3,4,41,42,43,44,45,46,47,48,49,50,51,52,55,58,59,],[38,-2,-3,-4,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,58,-37,-38,]),'COMA':([3,4,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,61,],[39,-2,-3,-4,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,39,60,-49,-37,-38,-50,]),'DOS_PUNTOS':([5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[40,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,]),'INTEGER':([40,54,60,],[44,44,44,]),'FLOAT':([40,54,60,],[45,45,45,]),'BOOL':([40,54,60,],[46,46,46,]),'NULL':([40,54,60,],[47,47,47,]),'FECHA':([40,54,60,],[48,48,48,]),'EMAIL':([40,54,60,],[49,49,49,]),'URL':([40,54,60,],[50,50,50,]),'CORCHETE_IZQ':([40,54,60,],[54,54,54,]),'CORCHETE_DER':([43,44,45,46,47,48,49,50,51,52,56,57,58,59,61,],[-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,59,-49,-37,-38,-50,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'json':([0,],[1,]),'elementos':([2,53,],[3,55,]),'par':([2,39,53,],[4,41,4,]),'clave':([2,39,53,],[5,5,5,]),'valor':([40,54,60,],[42,57,61,]),'objeto':([40,54,60,],[51,51,51,]),'lista':([40,54,60,],[52,52,52,]),'valores':([54,],[56,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> json","S'",1,None,None,None),
  ('json -> LLAVE_IZQ elementos LLAVE_DER','json',3,'p_json','lexer_parser.py',158),
  ('elementos -> par','elementos',1,'p_elementos','lexer_parser.py',166),
  ('elementos -> elementos COMA par','elementos',3,'p_elementos','lexer_parser.py',167),
  ('par -> clave DOS_PUNTOS valor','par',3,'p_par','lexer_parser.py',177),
  ('clave -> STRING','clave',1,'p_clave','lexer_parser.py',234),
  ('clave -> CLAVE_LINK','clave',1,'p_clave','lexer_parser.py',235),
  ('clave -> CLAVE_EMAIL','clave',1,'p_clave','lexer_parser.py',236),
  ('clave -> LISTA_EQUIPOS','clave',1,'p_clave','lexer_parser.py',237),
  ('clave -> NOMBRE_EQUIPO','clave',1,'p_clave','lexer_parser.py',238),
  ('clave -> IDENTIDAD_EQUIPO','clave',1,'p_clave','lexer_parser.py',239),
  ('clave -> ASIGNATURA','clave',1,'p_clave','lexer_parser.py',240),
  ('clave -> CARRERA','clave',1,'p_clave','lexer_parser.py',241),
  ('clave -> UNIVERSIDAD_REGIONAL','clave',1,'p_clave','lexer_parser.py',242),
  ('clave -> DIRECCION','clave',1,'p_clave','lexer_parser.py',243),
  ('clave -> ALIANZA_EQUIPO','clave',1,'p_clave','lexer_parser.py',244),
  ('clave -> INTEGRANTES','clave',1,'p_clave','lexer_parser.py',245),
  ('clave -> PROYECTOS','clave',1,'p_clave','lexer_parser.py',246),
  ('clave -> NOMBRE','clave',1,'p_clave','lexer_parser.py',247),
  ('clave -> EDAD','clave',1,'p_clave','lexer_parser.py',248),
  ('clave -> CARGO','clave',1,'p_clave','lexer_parser.py',249),
  ('clave -> FOTO','clave',1,'p_clave','lexer_parser.py',250),
  ('clave -> HABILIDADES','clave',1,'p_clave','lexer_parser.py',251),
  ('clave -> SALARIO','clave',1,'p_clave','lexer_parser.py',252),
  ('clave -> ACTIVO','clave',1,'p_clave','lexer_parser.py',253),
  ('clave -> ESTADO','clave',1,'p_clave','lexer_parser.py',254),
  ('clave -> RESUMEN','clave',1,'p_clave','lexer_parser.py',255),
  ('clave -> TAREAS','clave',1,'p_clave','lexer_parser.py',256),
  ('clave -> FECHA_INICIO','clave',1,'p_clave','lexer_parser.py',257),
  ('clave -> FECHA_FIN','clave',1,'p_clave','lexer_parser.py',258),
  ('clave -> VIDEO','clave',1,'p_clave','lexer_parser.py',259),
  ('clave -> CONCLUSION','clave',1,'p_clave','lexer_parser.py',260),
  ('clave -> CALLE','clave',1,'p_clave','lexer_parser.py',261),
  ('clave -> CIUDAD','clave',1,'p_clave','lexer_parser.py',262),
  ('clave -> PAIS','clave',1,'p_clave','lexer_parser.py',263),
  ('clave -> VERSION','clave',1,'p_clave','lexer_parser.py',264),
  ('clave -> FIRMA_DIGITAL','clave',1,'p_clave','lexer_parser.py',265),
  ('objeto -> LLAVE_IZQ elementos LLAVE_DER','objeto',3,'p_objeto','lexer_parser.py',270),
  ('lista -> CORCHETE_IZQ valores CORCHETE_DER','lista',3,'p_lista','lexer_parser.py',288),
  ('valor -> STRING','valor',1,'p_valor','lexer_parser.py',293),
  ('valor -> INTEGER','valor',1,'p_valor','lexer_parser.py',294),
  ('valor -> FLOAT','valor',1,'p_valor','lexer_parser.py',295),
  ('valor -> BOOL','valor',1,'p_valor','lexer_parser.py',296),
  ('valor -> NULL','valor',1,'p_valor','lexer_parser.py',297),
  ('valor -> FECHA','valor',1,'p_valor','lexer_parser.py',298),
  ('valor -> EMAIL','valor',1,'p_valor','lexer_parser.py',299),
  ('valor -> URL','valor',1,'p_valor','lexer_parser.py',300),
  ('valor -> objeto','valor',1,'p_valor','lexer_parser.py',301),
  ('valor -> lista','valor',1,'p_valor','lexer_parser.py',302),
  ('valores -> valor','valores',1,'p_valores','lexer_parser.py',309),
  ('valores -> valores COMA valor','valores',3,'p_valores','lexer_parser.py',310),
]
