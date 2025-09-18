import re

def dividir_por_estructura(texto):
    libros = re.split(r"(LIBRO\s+[IVXLCDM]+.*?)\n", texto, flags=re.IGNORECASE)
    resumen = {}

    for i in range(1, len(libros), 2):
        nombre_libro = libros[i].strip()
        contenido_libro = libros[i+1]

        titulos = re.split(r"(T[ÍI]TULO\s+[IVXLCDM]+.*?)\n", contenido_libro, flags=re.IGNORECASE)
        resumen_libro = {}

        for j in range(1, len(titulos), 2):
            nombre_titulo = titulos[j].strip()
            contenido_titulo = titulos[j+1][:1000]  # resumen inicial
            resumen_libro[nombre_titulo] = contenido_titulo.strip()

        resumen[nombre_libro] = resumen_libro

    return resumen
