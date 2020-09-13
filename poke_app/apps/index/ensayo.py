import numpy as np
import pandas as pd
import easygui as easygui
from . import parse_funcion
import os

extension = ["*.txt","*.csv"]
pd.options.display.max_columns = None

def main(archivo): 
    # archivo = eg.fileopenbox(msg="Abrir archivo",
    #                      title="Control: fileopenbox",
    #                      default='',
    #                      filetypes=extension)
    archivo = ('diagramas/'+archivo)
    archivo = os.path.abspath(archivo)
    data = pd.read_csv(archivo)
    print(data)
    data = parse_funcion.depurar(data)
    data.dropna(axis=1,how='all',inplace=True)
    print(data,'\n')
    print(parse_funcion.add_origen_destino(data))
    data.to_json(r'json.json', orient='records') #Crear json