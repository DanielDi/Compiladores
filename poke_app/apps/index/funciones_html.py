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
        "' name='"+ nombre +"' value='"+opcion+str(id_etiqueta)+"'>" + opcion)
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