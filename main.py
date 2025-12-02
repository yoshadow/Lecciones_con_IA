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


def generar_leccion_ceaec(instrucciones: str, texto_pdf: str) -> str:
    """
    Genera una lección completa CEAEC usando:
    - Instrucciones del archivo Instrucciones_LEGO.txt
    - Fragmento del PDF modelo
    - Datos propios de la tabla de la lección
    """

    client = OpenAI()

    prompt_usuario = f"""
{instrucciones}

Analiza la siguiente información para crear la lección 2 de Robótica con LEGO. 
El grado es PRIMARIA BAJA.

===========================
DATOS DE LA LECCIÓN:
===========================

Lección: 2  
Título de la lección: Pateador  
Identificador: TS_WeDo_L02  
Área de contenido: Ciencia, Ingeniería  
Tema: Robots que reaccionan a estímulos  
Recursos digitales: Software WeDo 2.0  
Materiales: Kit Educativo compatible con WeDo 2.0  
Contenidos: Engranajes y sensor de proximidad  
Objetivos de aprendizaje: Activar un mecanismo de patada cuando el robot detecta un objeto cercano  
Habilidades: Pensamiento crítico, experimentación, trabajo colaborativo  
Competencia STEAM:
- Ciencia: sensores y reacciones
- Ingeniería: transmisión de movimiento
Actividad de exploración: Colocar un objeto frente al sensor para activar la patada  
Actividad complementaria base: Cambiar el tamaño de los engranajes para que la patada sea más fuerte o más suave  

===========================
INSTRUCCIONES GENERALES:
===========================

Genera una propuesta de lección completa siguiendo EXACTAMENTE las etapas de la metodología CEAEC.
Desarrolla todas las etapas como si estuvieran escritas en un LIBRO DEL ALUMNO.

Incluye:

1. Una TABLA INICIAL con:
   - Número de lección
   - Título de la lección
   - Identificador
   - Nivel
   - Objetivo
   - Habilidades
   - Materiales (texto fijo):
     “Kit de robótica educativa con ladrillos y Software WeDo 2.0”

===========================
SECCIÓN DEL PROFESOR:
===========================

Al final agrega:
**"Instrucciones para el profesor"**

Incluye instrucciones para cada etapa CEAEC redactadas:
- en modo imperativo  
- segunda persona (“tú”)  
- listas con viñetas  

===========================
ACTIVIDADES COMPLEMENTARIAS:
===========================

Agrega 2 actividades complementarias adicionales (20 minutos cada una).
No desarrolladas, solo descritas en modo imperativo para el alumno.

===========================

Ahora complementa todo lo anterior con el estilo del siguiente fragmento del PDF:

\"\"\"{texto_pdf[:2500]}\"\"\"
"""

    respuesta = client.chat.completions.create(
        model="gpt-5.1",
        messages=[
            {"role": "system", "content": "Eres un experto en diseño de lecciones LEGO con metodología CEAEC."},
            {"role": "user", "content": prompt_usuario},
        ],
        temperature=0.4,
        max_completion_tokens=3500,
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

    # 4) Generar la lección completa con metodología CEAEC
    print("\n" + "=" * 60)
    print("🚀 Generando lección completa CEAEC para la lección 2: Pateador...")

    leccion_completa = generar_leccion_ceaec(instrucciones, texto_pdf)

    # Guardar la lección en un archivo Markdown
    nombre_archivo_salida = "L02_Pateador_PrimariaBaja_CEAEC.md"

    with open(nombre_archivo_salida, "w", encoding="utf-8") as f:
        f.write(leccion_completa)

    print(f"\n✅ Lección generada y guardada en: {nombre_archivo_salida}")
    print("Puedes abrir ese archivo en VS Code para revisarla con calma.")


if __name__ == "__main__":
    main()
