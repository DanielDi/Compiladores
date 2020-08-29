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
    data.dropna(axis=1,how='all',inplace=True)
    #print(data)
    #print(get_evento_inicio(data))
    #print(get_grupos_vistas(data))
    print(on_vista(data,get_grupos_vistas(data).id))

if __name__ == "__main__": 
    main() 
