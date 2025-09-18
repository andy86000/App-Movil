import pdfplumber

def extraer_texto_pdf(ruta_pdf):
    texto_total = ""
    with pdfplumber.open(ruta_pdf) as pdf:
        for pagina in pdf.pages:
            contenido = pagina.extract_text()
            if contenido:
                texto_total += contenido + "\n"
    return texto_total
