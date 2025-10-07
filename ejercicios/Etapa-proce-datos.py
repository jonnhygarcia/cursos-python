# Etapas de procecsamiento de datos: recopilación, limpieza, transformación, análisis e interpretación.
# Ejemplo simple de cada etapa usando Python
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
# 1. Recopilación de datos: Cargar datos desde un archivo CSV
datos = pd.read_csv('./ejemplos/datos.csv')
print("Datos recopilados:")
print(datos.head()) # Muestra las primeras filas del DataFrame
