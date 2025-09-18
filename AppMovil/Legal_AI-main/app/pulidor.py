import re

def limpiar_texto(texto):
    """
    Limpia saltos de línea, espacios repetidos, referencias cruzadas, etc.
    """
    texto = re.sub(r'\n+', ' ', texto)  # unifica líneas
    texto = re.sub(r'\s{2,}', ' ', texto)  # elimina espacios repetidos
    texto = texto.strip()
    return texto

def extraer_articulos_clave(contenido, max_articulos=2, max_lineas=5):
    """
    Extrae los primeros 'max_articulos' que empiecen con 'Art.' o 'ART.'
    y limita su contenido a 'max_lineas' por artículo.
    """
    # Detectar artículos por regex
    articulos = re.split(r'(Art\.?\s+\d+[.-]?)', contenido, flags=re.IGNORECASE)
    resultado = []

    for i in range(1, len(articulos), 2):
        encabezado = articulos[i].strip()
        cuerpo = limpiar_texto(articulos[i+1]) if i+1 < len(articulos) else ""
        lineas = cuerpo.split('. ')
        cuerpo_resumido = '. '.join(lineas[:max_lineas]) + '.' if lineas else ''
        resultado.append(f"{encabezado} {cuerpo_resumido}".strip())

        if len(resultado) >= max_articulos:
            break

    return '\n'.join(resultado) if resultado else limpiar_texto(contenido[:600])  # fallback

def refinar_resumen(resumen_raw, max_articulos=2, max_lineas=5):
    """
    Aplica refinamiento a cada sección del resumen estructurado.
    """
    resumen_refinado = {}
    for libro, titulos in resumen_raw.items():
        titulos_refinados = {}
        for titulo, contenido in titulos.items():
            refinado = extraer_articulos_clave(contenido, max_articulos, max_lineas)
            titulos_refinados[titulo] = refinado
        resumen_refinado[libro] = titulos_refinados
    return resumen_refinado
