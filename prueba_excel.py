import os
import re
import pandas as pd

# Expresión regular que deseas buscar
expresion_regular = re.compile(r'combustible', re.IGNORECASE)  # Ignorar mayúsculas/minúsculas

# Directorio donde se encuentran los archivos Excel
directorio = './archivos/'

# Lista para almacenar las filas coincidentes
filas_coincidentes = []

# Función para buscar en archivos Excel (CSV y XLSX)
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
                            break  # Rompe el bucle para evitar duplicados
    except Exception as e:
        print(f'Error al procesar {archivo_path}: {e}')

# Bucle a través de los archivos en el directorio y sus subdirectorios
for root, dirs, files in os.walk(directorio):
    for file in files:
        archivo_path = os.path.join(root, file)
        if archivo_path.endswith('.csv') or archivo_path.endswith('.xlsx'):
            buscar_en_excel(archivo_path)

# Crear un DataFrame con las filas coincidentes
if filas_coincidentes:
    df_coincidentes = pd.DataFrame(filas_coincidentes)
    # Exportar el DataFrame a un archivo Excel
    nombre_archivo_salida = 'filas_coincidentes.xlsx'
    df_coincidentes.to_excel(nombre_archivo_salida, index=False)
    print(f'Las filas coincidentes se han exportado a {nombre_archivo_salida}')
else:
    print("No se encontraron filas coincidentes.")

print(list(filas_coincidentes[0]))
print(filas_coincidentes[0])