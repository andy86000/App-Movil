import streamlit as st
from app.extractor import extraer_texto_pdf
from app.estructura import dividir_por_estructura
from app.pulidor import refinar_resumen
from app.resumen import construir_resumen
from app.exportador import exportar_a_word
import os

st.set_page_config(page_title="Resumen Legal IA", layout="wide")
st.title("📘 Generador de Resúmenes de Documentos Legales")

st.markdown("Sube un archivo PDF legal para extraer su contenido, estructurarlo por libros/títulos/artículos y generar un resumen exportable.")

uploaded_file = st.file_uploader("📄 Sube tu documento legal en formato PDF", type=["pdf"])

if uploaded_file:
    # Guardar archivo temporal
    temp_path = os.path.join("docs", uploaded_file.name)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success("✅ Documento cargado correctamente")

    # Extraer texto
    with st.spinner("🔍 Extrayendo texto del PDF..."):
        texto = extraer_texto_pdf(temp_path)

    if texto:
        st.subheader("🧾 Texto extraído (primeros 1000 caracteres)")
        st.text(texto[:1000])

        # Procesar estructura
        estructura = dividir_por_estructura(texto)
        estructura_refinada = refinar_resumen(estructura)
        resumen = construir_resumen(estructura_refinada)

        st.subheader("📑 Resumen estructurado")
        st.text_area("Resultado", resumen, height=400)

        # Exportar a Word
        if st.button("💾 Exportar resumen a Word"):
            nombre = "outputs/resumen_legal.docx"
            exportar_a_word(resumen, nombre)
            with open(nombre, "rb") as f:
                st.download_button("📥 Descargar resumen", data=f, file_name="resumen_legal.docx")
    else:
        st.warning("No se pudo extraer texto del PDF.")
