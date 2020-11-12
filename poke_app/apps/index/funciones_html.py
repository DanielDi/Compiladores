from django.conf import settings
import sqlite3
from sqlite3 import Error

# Funciones que reciben un objeto JSON del TIPO de elemento HTML que el 
# usuario desea crear 

def crearFormulario(form_json, idForm, mi_json):
  idFormulario = form_json["id"]
  almacen = None
  for obj in mi_json:
    if obj["Destino"] == idFormulario and obj["Nombre"] == "Almacén de datos":
      almacen = obj
      break

  nombreTabla = None
  if(almacen):
    nombreTabla = almacen["Texto1"]

  if(nombreTabla):
    formulario = "<h3>" + form_json['Texto1'] + "</h3>" + "<form id='" + idForm + "' name='" + nombreTabla + "'>"

  else:
    formulario = "<h3>" + form_json['Texto1'] + "</h3>" + "<form id='" + idForm + "'>"

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
      entrada = "<input type='" + tipo + "' id='" + idForm + "." + str(id_etiqueta) + "' name='" + nombre + "'><br>"
      id_etiqueta += 1
    formulario += label + entrada

  formulario += "</form>"
  return formulario

def crearBoton(boton_json, idBoton):
  boton = "<button type='button' id='" + idBoton + "'>" + boton_json['Texto1'] + "</button>"
  return boton

def crearSentenciaTablas(almacen, mi_json):
  idAlmacen = almacen["id"]
  nombreTabla = almacen["Texto1"]

  for obj in mi_json:
    if obj["id"] == almacen["Destino"]:
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
    elif tipoCol[:8] == "checkbox":
      tipoCol = "text"
    elif tipoCol[:5] == "radio":
      tipoCol = "text"
    
    sentenciaSQL += nombreCol + " " + tipoCol + ",\n"

  sentenciaSQL = sentenciaSQL[:-2]
  sentenciaSQL += ");"
  print(sentenciaSQL) 

  conn = create_connection(settings.DATABASES['default']['NAME'])
  create_table(conn, sentenciaSQL)
  conn.close()


def crearSentenciaInsert(datos_json):
  sentencia = "INSERT INTO " + datos_json["tabla"] + "("
  del datos_json["tabla"]
  print("DATOS DENTRO DE LA FUNC INSERT")
  print(datos_json)

  for key in datos_json:
    sentencia += key + ","

  sentencia = sentencia[:-1] + ") VALUES("

  for key in datos_json:
    if(datos_json[key]):
      sentencia += "'" + datos_json[key] + "'" + ","
    else:
      sentencia += "null" + ","

  sentencia = sentencia[:-1] + ")"
  print("SENTENCIA INSERT FINAL:")
  print(sentencia)

  conn = create_connection(settings.DATABASES['default']['NAME'])
  cur = conn.cursor()
  cur.execute(sentencia)
  conn.commit()
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
  



