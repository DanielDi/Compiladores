from django.conf import settings
import sqlite3
from sqlite3 import Error

# Funciones que reciben un objeto JSON del TIPO de elemento HTML que el 
# usuario desea crear 

def crearFormulario(form_json, idForm):
  formulario = "<h3>" + form_json['Texto1'] + "</h3>" + "<form action=''>"
  campos = (form_json['campos']).split(';')
  id_etiqueta = 1
  for campo in campos:
    entrada = ""
    nombre, tipo = campo.split(':')
    label = "<label for='" + idForm + "." + str(id_etiqueta) + "'>" + nombre +":" + "</label><br>"
    #radio(pollo,res,cerdo,humano)
    #Verificar si tipo de elemento es radio y checkbox. de caso contrario lo hace noraml
    if "(" in tipo:
      tipo, opciones = tipo.split('(')
      opciones = opciones[:-1].split(',')
      for opcion in opciones:
        entrada += ("<input type='" + tipo + "' id='" + idForm + "." + str(id_etiqueta) + 
        "' name='"+ nombre +"' value='"+opcion+"'>" + opcion)
        id_etiqueta += 1
      if tipo == "radio":
        entrada = entrada[:(len(opcion)+1)*-1] + "required" + ">" + opcion + "<br>"
      else:
        entrada += "<br>"
    else:    
      entrada = "<input type='" + tipo + "' id='" + idForm + "." + str(id_etiqueta) + "'><br>"
      id_etiqueta += 1
    formulario += label + entrada

  formulario += "<br><input type='submit' value='Enviar'></form>"
  return formulario

def crearBoton(boton_json, idBoton):
  boton = "<button type='button' id='" + idBoton + "'>" + boton_json['Texto1'] + "</button>"
  return boton

def crearTablas(almacen, mi_json):
  idAlmacen = almacen["id"]
  nombreTabla = almacen["Texto1"]
  for obj in mi_json:
    if obj["Destino"] == idAlmacen and obj["Nombre"] == "Línea":
      idFormulario = obj["Origen"]
      break

  for obj in mi_json:
    if obj["id"] == idFormulario:
      formulario = obj
      break 

  campos = (formulario['campos']).split(';')
  nombre_y_tipo = []

  for campo in campos:
    nombre_y_tipo += [campo.split(':')]

  sentenciaSQL = "CREATE TABLE IF NOT EXISTS " + nombreTabla + " (\n"

  for columna in nombre_y_tipo:
    nombreCol, tipoCol = columna
    if tipoCol == "number":
      tipoCol = "real"
    
    sentenciaSQL += nombreCol + " " + tipoCol + ",\n"

  sentenciaSQL = sentenciaSQL[:-2]
  sentenciaSQL += ");"
  print(sentenciaSQL) 

  conn = create_connection(settings.DATABASES['default']['NAME'])
  create_table(conn, sentenciaSQL)
  conn.close()

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
  
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
  
