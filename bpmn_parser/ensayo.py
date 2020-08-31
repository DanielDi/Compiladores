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
    print(add_origen_destino(data))
    data.to_json(r'json.json', orient='records') #Crear json

if __name__ == "__main__":
    main()