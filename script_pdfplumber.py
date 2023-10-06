import pdfplumber
import re
import os

directorio = 'listas'
patron = r'Poxilina'
palabra = ""

def buscar_pdf(archivo_path):
    with pdfplumber.open(archivo_path) as pdf:
        # Itera a través de todas las páginas
        for page in pdf.pages:
            # Extrae el texto de la página
            page_text = page.extract_text()
            # Divide el texto en líneas
            lines = page_text.split('\n')

        for line in lines:
            coincidencia = re.search(patron, line, re.IGNORECASE)
            if coincidencia:
                print(f'LINEA: {line}')
                # Encontrar precios
                patron_precios = r'\d{1,5}(?:\.\d{3})*(?:,\d+)'
                precios = re.findall(patron_precios, line)
                print(f'PRECIO: {precios}')
                nombre = line
                for precio in precios:
                    nombre = nombre.replace(precio, "")
                print(f'NOMBRE: {nombre}')
                print(f'ARCHIVO: {os.path.basename(archivo_path)}')
                #input("Presione una tecla para continuar")
                print("-------------------------------")


# Buscar en el directorio y sus subdirectorios
for root, dirs, files in os.walk(directorio):
    for file in files:
        archivo_path = os.path.join(root, file)
        if archivo_path.endswith('.pdf'):
            buscar_pdf(archivo_path)






#with pdfplumber.open('listas\lista_poxipol.pdf') as pdf:
#    # Itera a través de todas las páginas
#    for page in pdf.pages:
#        # Extrae el texto de la página
#        page_text = page.extract_text()
#
#        # Divide el texto en líneas
#        lines = page_text.split('\n')
#
#        for line in lines:
#            print(f'LINEA: {line}')
#            # Encontrar precios
#            patron_precios = r'\d{1,5}(?:\.\d{3})*(?:,\d+)'
#            precios = re.findall(patron_precios, line)
#            print(f'PRECIO: {precios}')
#            nombre = line
#            for precio in precios:
#                nombre = nombre.replace(precio, "")
#            print(f'NOMBRE: {nombre}')
#            input("Presione una tecla para continuar")
#            print("-------------------------------")








