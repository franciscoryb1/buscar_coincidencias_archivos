# import aspose.pdf as ap
# input_pdf = "prueba_pdf_to_xlsx\prueba_pdf_2.pdf"
# output_pdf = "prueba_pdf_to_xlsx\prueba_salida.xlsx"


# # Open PDF document
# document = ap.Document(input_pdf)
# save_option = ap.ExcelSaveOptions()
# # Save the file into MS Excel format
# document.save(output_pdf, save_option)



import PyPDF2
import pandas as pd

# Ruta al archivo PDF de entrada
input_pdf = "prueba_pdf_to_xlsx\prueba_pdf.pdf"

# Crear un objeto PDFFileReader
pdf_reader = PyPDF2.PdfFileReader(open(input_pdf, "rb"))

# Crear una lista para almacenar el texto extraído de cada página
pdf_text = []

# Iterar a través de las páginas del PDF y extraer el texto
for page_num in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(page_num)
    pdf_text.append(page.extractText())

# Crear un DataFrame de pandas con el texto extraído
df = pd.DataFrame(pdf_text, columns=["Texto"])

# Ruta al archivo XLSX de salida
output_xlsx = "output.xlsx"

# Guardar el DataFrame en un archivo XLSX
df.to_excel(output_xlsx, index=False, engine='openpyxl')

print(f"El PDF se ha convertido a XLSX y se ha guardado en {output_xlsx}")


