import pandas as pd
import numpy as np

def depurar(df):
    #Eliminar columnas innecesarias
    df.drop(['Biblioteca de figuras','ID de página','Flecha de origen','Flecha de destino'], axis = 'columns', inplace=True)

    #Renombrar algunas columnas
    df.rename(columns={'Origen de línea':'Origen', 'Destino de la línea':'Destino', 'Área de texto 1':'Texto1'}, inplace=True)

    #Eliminar filas innecesarias
    df = df.drop(df[df['Nombre']=='Página'].index)

    df.dropna(axis=1,how='all',inplace=True)
    return (df)

#añadir los origenes y destinos con base en la información de las líneas
def add_origen_destino(df):
    #Se reemplaza el destino del almacenamiento por el id de su respectivo formulario
    # almacenamientos = df[(df['Nombre']=='Almacén de datos')]
    # for _,row in almacenamientos.iterrows():
    #     df.loc[(df.id == row['id']), 'Destino'] = df[df.Destino == row.id].Origen.item() 
    #     #Se elimina la línea entre el almacenamiento y el formulario 
    #     df = df.drop(df[df.Destino == row.id].index)

    # condicionales = df[(df['Nombre']=='Gateway')]
    # for _,row in almacenamientos.iterrows():
    #     valores = df[(df.Origen == row['id'] and df.Nombre != "Línea")]
    #     for _,row2 in valores:
    #         df.loc[(df.Origen == row2['id'] and df.Nombre != "Línea"), 'ValorVerdad'] = df[df.Destino == row2.id and df.Nombre == "Línea"].Texto1.item()
        

    lineas = df[(df['Nombre']=='Línea')].dropna(axis=1)
    for _,row in lineas.iterrows():
        print(df[(df.id == row.Destino)].Nombre.item())
        if df[(df.id == row.Destino)].Nombre.item() == "Almacén de datos":
            df.loc[(df.id == row['Destino']), 'Destino'] = df.loc[df.id == row.id].Origen.item()

        elif df[(df.id == row.Origen)].Nombre.item() == "Gateway":
            df.loc[(df.id == row.Destino), "valorVerdad"] = df.loc[df.id == row.id].Texto1.item()
            df.loc[(df.id == row['Destino']), 'Origen'] = row['Origen']
            df.loc[(df.id == row['Origen']), 'Destino'] = row['Destino']

        else:
            df.loc[(df.id == row['Destino']), 'Origen'] = row['Origen']
            df.loc[(df.id == row['Origen']), 'Destino'] = row['Destino']

    df = df.drop(df[(df.Nombre == 'Línea')].index)

    #Bloque para convertir lineas en botones
    # lineas = df[(df.Nombre == 'Línea') & (df.Texto1.notna())]
    # df = df.drop(df[(df.Nombre == 'Línea')].index)
    # add = []
    # id = df.id.max()+1
    # for _,row in lineas.iterrows():
    #     df.Origen = df.Origen.replace({row['Origen']:id})
    #     add.append({'id':id, 'Nombre' : 'Línea' , 'Texto1' : row['Texto1'], 'Origen':row['Origen'], 'Destino':row['Destino']})
    #     id += 1
    # for i in add:
    #     df = df.append(i, ignore_index=True)

    return(df)

#Dice que elementos estan en una vista (o grupo)
def on_vista(df,vista):
    return (df[df['Contenido por'] == float(vista)].dropna(axis=1))

#Obtener todas las vistas en el modelo
def get_grupos_vistas(df):
    return (df[(df['Nombre']=='Grupo')].dropna(axis=1))

def get_tarea(df):
    return (df[(df['Nombre']=='Tarea') & (df['tipo'].isnull())].dropna(axis=1))

def get_tarea_usuario(df):
    return (df[(df['Nombre']=='Tarea') & (df['tipo']=='Usuario')].dropna(axis=1))

def get_tarea_enviar(df):
    return (df[(df['Nombre']=='Tarea') & (df['tipo']=='Enviar')].dropna(axis=1))

def get_evento_inicio(df):
    return (df[(df['Nombre']=='Evento de inicio') & (df['tipo']=='Inicio')].dropna(axis=1))

def get_evento_intermedio(df):
    return (df[(df['Nombre']=='Evento de inicio') & (df['tipo']=='Intermedio')].dropna(axis=1))

def get_evento_fin(df):
    return (df[(df['Nombre']=='Evento de inicio') & (df['tipo']=='Fin')].dropna(axis=1))