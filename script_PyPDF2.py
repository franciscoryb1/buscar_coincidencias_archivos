import PyPDF2
import re

# Abre el archivo PDF en modo lectura binaria
with open('listas\lista_fram.pdf', 'rb') as pdf_file:
    # Crea un objeto PDFReader
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    # Número total de páginas en el PDF
    num_pages = len(pdf_reader.pages)
    # Itera a través de todas las páginas
    for page_num in range(2):
        # Obtiene una página específica
        page = pdf_reader.pages[page_num]
        # Extrae el texto de la página
        page_text = page.extract_text()



        for line in page.extract_text().split("\n"):
            print(f'LINEA: {line}')
            # Encontrar precios
            patron_precios = r'\d{1,5}(?:\.\d{3})*(?:,\d+)'
            precios = re.findall(patron_precios, line)
            for precio in precios:
                print(f'PRECIO: {precio}')
                nombre = line.replace(precio, "")
                print(f'NOMBRE: {nombre}')
            input("Presione una tecla para continuar")
            print("-------------------------------")