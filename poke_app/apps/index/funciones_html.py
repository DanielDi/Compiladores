# Funciones que reciben un objeto JSON del TIPO de elemento HTML que el 
# usuario desea crear 

def crearFormulario(form_json, idForm):
  formulario = "<h3>" + form_json['Texto1'] + "</h3>" + "<form action=''>"
  campos = (form_json['campos']).split(';')
  id_etiqueta = 1
  for campo in campos:
    nombre, tipo = campo.split(':')
    label = "<label for='" + idForm + "." + str(id_etiqueta) + "'>" + nombre + "</label><br>"
    entrada = "<input type='" + tipo + "' id='" + idForm + "." + str(id_etiqueta) + "'><br>"
    formulario += label + entrada
    id_etiqueta += 1

  formulario += "<br><input type='submit' value='Enviar'></form>"
  return formulario

def crearBoton(boton_json, idBoton):
  boton = "<button type='button' id='" + idBoton + "'>" + boton_json['Texto1'] + "</button>"
  return boton