def construir_resumen(resumen_estructura):
    resumen = ""
    for libro, titulos in resumen_estructura.items():
        resumen += f"\n📘 {libro}\n"
        for titulo, contenido in titulos.items():
            resumen += f"\n🔹 {titulo}\n"
            resumen += contenido + "\n"
    return resumen
