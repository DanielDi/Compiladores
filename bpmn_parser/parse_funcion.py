import pandas as pd

def get_evento_inicio(df):
    return (df[(df['Nombre']=='Evento de inicio') & (df['tipo']=='Inicio')].dropna(axis=1))

def get_grupos_vistas(df):
    return (df[(df['Nombre']=='Grupo')].dropna(axis=1))

def on_vista(df,vista):
    return (df[df['Contenido por'] == float(vista)].dropna(axis=1))