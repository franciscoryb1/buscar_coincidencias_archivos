import os
import re
import pandas as pd
import math

expresion_regular = re.compile(r'poxil', re.IGNORECASE)

directorio = './archivos/'

filas_coincidentes = []

def buscar_en_excel(archivo_path):
    try:
        if archivo_path.endswith('.csv'):
            df = pd.read_csv(archivo_path)
        elif archivo_path.endswith('.xlsx'):
            xls = pd.ExcelFile(archivo_path)
            for sheet_name in xls.sheet_names:
                df = pd.read_excel(xls, sheet_name=sheet_name)
                for index, row in df.iterrows():
                    for columna, valor in row.items():
                        if isinstance(valor, str) and expresion_regular.search(valor):
                            filas_coincidentes.append(row)
                            break
    except Exception as e:
        print(f'Error al procesar {archivo_path}: {e}')

# Buscar en el directorio y sus subdirectorios
for root, dirs, files in os.walk(directorio):
    for file in files:
        archivo_path = os.path.join(root, file)
        if archivo_path.endswith('.csv') or archivo_path.endswith('.xlsx'):
            buscar_en_excel(archivo_path)

# Crear un DataFrame con las filas coincidentes
# if filas_coincidentes:
#     df_coincidentes = pd.DataFrame(filas_coincidentes)
#     nombre_archivo_salida = 'filas_coincidentes.xlsx'
#     df_coincidentes.to_excel(nombre_archivo_salida, index=False)
#     print(f'Las filas coincidentes se han exportado a {nombre_archivo_salida}')
# else:
#     print("No se encontraron filas coincidentes.")

# print(list(filas_coincidentes[0]))
# print(list(filas_coincidentes[1]))
# print(len(filas_coincidentes))
# for i in range(len(filas_coincidentes)):
#     print(list(filas_coincidentes[i]))


# Lista

salida = []
for i in range(len(filas_coincidentes)):
    fila = list(filas_coincidentes[i])
    nombre = ""
    precios = []
    for x in fila:
        if isinstance(x, float):
            precios.append(x)
        elif isinstance(x, str):
            nombre = nombre + " " + x
    precios = [y for y in precios if not math.isnan(y)]
    salida.append([nombre, precios])

for sal in salida:
    print(sal)



# Diccionario

# salida = {}
# for i in range(len(filas_coincidentes)):
#     fila = list(filas_coincidentes[i])
#     nombre = ""
#     precios = []
#     for x in fila:
#         if isinstance(x, float):
#             precios.append(x)
#         elif isinstance(x, str):
#             nombre = nombre + " " + x
#     precios = [y for y in precios if not math.isnan(y)]
#     salida[nombre] = precios

# print(salida)