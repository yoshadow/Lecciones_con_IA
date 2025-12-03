# main.py
import os
from pathlib import Path

from dotenv import load_dotenv
from PyPDF2 import PdfReader

from openai import OpenAI

def cargar_instrucciones() -> str:
    """
    Lee el archivo Instrucciones_LEGO.txt que está en la misma carpeta
    que main.py y devuelve su contenido como texto.
    """
    ruta_base = Path(__file__).parent  # carpeta donde está main.py
    ruta_instrucciones = ruta_base / "Instrucciones_LEGO.txt"

    if not ruta_instrucciones.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_instrucciones}")

    texto = ruta_instrucciones.read_text(encoding="utf-8")
    return texto


def leer_pdf_modelo() -> str:
    """
    Lee el archivo PDF de ejemplo ubicado en pdfs/leccion_modelo.pdf
    y devuelve todo el texto extraído.
    """
    ruta_base = Path(__file__).parent
    ruta_pdf = ruta_base / "pdfs" / "TS_WeDo_L01.pdf"

    if not ruta_pdf.exists():
        raise FileNotFoundError(f"No se encontró el PDF: {ruta_pdf}")

    texto = ""
    with ruta_pdf.open("rb") as f:
        lector = PdfReader(f)
        for pagina in lector.pages:
            pagina_texto = pagina.extract_text() or ""
            texto += pagina_texto + "\n"

    return texto


def probar_llamada_openai(instrucciones: str, texto_pdf: str):
    """
    Realiza una prueba de conexión con OpenAI usando tus instrucciones
    y un fragmento del PDF modelo.
    """
    client = OpenAI()  # lee la API key desde el .env

    prompt_usuario = f"""
Usa las siguientes instrucciones como guía:

{instrucciones}

Ahora, basándote en el siguiente fragmento del PDF modelo:

\"\"\"{texto_pdf[:1000]}\"\"\"

Genera un texto breve (no una lección completa), solamente explicando
en 3 líneas cómo aplicarías la metodología CEAEC en una lección de prueba.
"""

    respuesta = client.chat.completions.create(
        model="gpt-5.1",
        messages=[
            {"role": "system", "content": "Eres un experto en robótica educativa con LEGO."},
            {"role": "user", "content": prompt_usuario},
        ],
        temperature=0.4,
        max_completion_tokens=300,
    )

    return respuesta.choices[0].message.content


def main():
    # 1) Cargar variables de entorno desde .env
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("⚠️ No se encontró OPENAI_API_KEY en el archivo .env")
    else:
        print("✅ Entorno listo. OPENAI_API_KEY detectada.")

    # 2) Leer el archivo de instrucciones LEGO
    instrucciones = cargar_instrucciones()
    print("\n✅ Instrucciones_LEGO.txt leído correctamente.")
    print("Vista previa (primeros 300 caracteres):\n")
    print(instrucciones[:300])
    print("\n" + "=" * 60 + "\n")

    # 3) Leer el PDF de la lección modelo
    texto_pdf = leer_pdf_modelo()
    print("✅ PDF leccion_modelo.pdf leído correctamente.")
    print("Vista previa del PDF (primeros 500 caracteres):\n")
    print(texto_pdf[:500])

    print("\n" + "=" * 60)
    print("🔍 Probando conexión con OpenAI...")

    respuesta = probar_llamada_openai(instrucciones, texto_pdf)

    print("\n✅ Respuesta de OpenAI:")
    print(respuesta)


if __name__ == "__main__":
    main()
