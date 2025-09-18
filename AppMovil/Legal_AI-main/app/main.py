from app.extractor import extraer_texto_pdf
from app.estructura import dividir_por_estructura
from app.resumen import construir_resumen
from app.exportador import exportar_a_word
from app.pulidor import refinar_resumen


if __name__ == "__main__":
    ruta_pdf = "docs/codigo_penal.pdf"  # asegúrate de colocar aquí el nombre correcto del PDF
    texto = extraer_texto_pdf(ruta_pdf)
    estructura = dividir_por_estructura(texto)
    estructura_refinada = refinar_resumen(estructura, max_articulos=2, max_lineas=4)
    resumen = construir_resumen(estructura_refinada)
    exportar_a_word(resumen)
    print("✅ Resumen generado correctamente en outputs/resumen_legal.docx")
