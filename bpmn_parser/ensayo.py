import numpy as nppip 
import pandas as pd
import easygui as eg
from parse_funcion import *

extension = ["*.txt","*.csv"]
pd.options.display.max_columns = None

def main(): 
    archivo = eg.fileopenbox(msg="Abrir archivo",
                         title="Control: fileopenbox",
                         default='',
                         filetypes=extension)
    data = pd.read_csv(archivo)
    data = depurar(data)
    data.dropna(axis=1,how='all',inplace=True)
    print(data,'\n')
    print(get_evento_inicio(data),'\n')
    print(get_tarea(data),'\n')
    print(on_vista(data,get_grupos_vistas(data).id),'\n')
    data.to_json(r'json',orient='index')

if __name__ == "__main__": 
    main()