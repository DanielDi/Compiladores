import pandas as pd

def depurar(df):
    df.drop(['Biblioteca de figuras','ID de página'], axis = 'columns', inplace=True)
    df = df.drop(df[df['Nombre']=='Página'].index)
    return (df)

def get_evento_inicio(df):
    return (df[(df['Nombre']=='Evento de inicio') & (df['tipo']=='Inicio')].dropna(axis=1))

def get_grupos_vistas(df):
    return (df[(df['Nombre']=='Grupo')].dropna(axis=1))

def on_vista(df,vista):
    return (df[df['Contenido por'] == float(vista)].dropna(axis=1))
    
def get_tarea(df):
    return (df[(df['Nombre']=='Tarea')].dropna(axis=1))
