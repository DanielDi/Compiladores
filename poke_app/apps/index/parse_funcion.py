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
    lineas = df[(df['Nombre']=='Línea')].dropna(axis=1)
    for _,row in lineas.iterrows():
        df.loc[(df.id == row['Destino']), 'Origen'] = row['Origen']
        df.loc[(df.id == row['Origen']), 'Destino'] = row['Destino']

    #Bloque para convertir lineas en botones
    lineas = df[(df.Nombre == 'Línea') & (df.Texto1.notna())]
    df = df.drop(df[(df.Nombre == 'Línea')].index)
    add = []
    id = df.id.max()+1
    for _,row in lineas.iterrows():
        df.Origen = df.Origen.replace({row['Origen']:id})
        add.append({'id':id, 'Nombre' : 'Tarea' , 'Texto1' : row['Texto1'], 'Origen':row['Origen'], 'Destino':row['Destino']})
        id += 1
    for i in add:
        df = df.append(i, ignore_index=True)

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