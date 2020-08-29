import pandas as pd

def get_evento_inicio(df):
    return (df[(df['Nombre']=='Evento de inicio') & (df['tipo']=='Inicio')].dropna(axis=1))
