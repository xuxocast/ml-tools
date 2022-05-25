from modules.aux_export_json import export_json
import pandas as pd
import os

##########################################################################################
# Genera un DataFrame Aleatorio para usar como ejemplo
import numpy as np
df = pd.DataFrame(np.random.rand(10, 3), columns=['A', 'B', 'C'])

##########################################################################################
filename = os.path.join('..','data', 'dataframe.json')
# Archivo en donde se exportará el dataframe
file = open(filename,'w',encoding='UTF-8')

export_json(df,file)