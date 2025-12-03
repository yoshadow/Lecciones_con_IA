# main.py
import os
from pathlib import Path

from dotenv import load_dotenv
from PyPDF2 import PdfReader
from openai import OpenAI

import pandas as pd  # para leer el Excel


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
    Lee el archivo PDF de ejemplo ubicado en pdfs/TS_WeDo_L01.pdf
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


def leer_lecciones_desde_excel(nombre_archivo: str = "Ejemplo.xlsx") -> list[dict]:
    """
    Lee el archivo Excel con los datos de las lecciones.
    Devuelve una lista de diccionarios, uno por lección.
    """
    ruta_base = Path(__file__).parent
    ruta_excel = ruta_base / nombre_archivo

    if not ruta_excel.exists():
        raise FileNotFoundError(f"No se encontró el Excel: {ruta_excel}")

    # header=1 -> usa la segunda fila como nombres de columna
    df = pd.read_excel(ruta_excel, header=1)

    # Elimina filas totalmente vacías (por si hay espacios al final)
    df = df.dropna(how="all")

    # Convierte a lista de dicts
    lecciones = df.to_dict(orient="records")
    return lecciones


def generar_leccion_ceaec(instrucciones: str, texto_pdf: str, datos: dict, client: OpenAI) -> str:
    """
    Genera una lección completa CEAEC usando:
    - Instrucciones del archivo Instrucciones_LEGO.txt
    - Fragmento del PDF modelo
    - Datos de UNA fila del Excel (diccionario 'datos')
    """

    # Extraemos campos desde el diccionario 'datos'.
    leccion_num = datos.get("Lección", "")
    titulo_leccion = datos.get("Título de la lección", "")
    identificador = datos.get("Identificador", "")
    tipo = datos.get("Tipo", "PRIMARIA BAJA")  # si no hay columna "Tipo", usamos este valor por defecto
    area_contenido = datos.get("Área de contenido", "")
    tema = datos.get("Tema", "")
    recursos_digitales = datos.get("Recursos digitales", "")
    materiales = datos.get("Materiales", "")
    contenidos = datos.get("Contenidos", "")
    objetivos = datos.get("Objetivos de aprendizaje", "")
    habilidades = datos.get("Habilidades", "")
    competencia_steam = datos.get("Competencia STEAM", "")
    act_exploracion = datos.get("Actividad de exploración", "")
    act_complementaria_base = datos.get("Actividad complementaria", "")

    # Para no hacer el prompt gigantesco, recortamos un poco el PDF
    fragmento_pdf = texto_pdf[:2500]

    prompt_usuario = f"""
{instrucciones}

Analiza la siguiente información para crear la lección {leccion_num} de Robótica con LEGO. 
El grado es {tipo}.

===========================
DATOS DE LA LECCIÓN:
===========================

Lección: {leccion_num}  
Título de la lección: {titulo_leccion}  
Identificador: {identificador}  
Área de contenido: {area_contenido}  
Tema: {tema}  
Recursos digitales: {recursos_digitales}  
Materiales: {materiales}  
Contenidos: {contenidos}  
Objetivos de aprendizaje: {objetivos}  
Habilidades: {habilidades}  
Competencia STEAM:
{competencia_steam}
Actividad de exploración: {act_exploracion}  
Actividad complementaria base: {act_complementaria_base}  

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

\"\"\"{fragmento_pdf}\"\"\"
"""

    try:
        respuesta = client.responses.create(
            model="gpt-5.1",
            input=[
                {"role": "system", "content": "Eres un experto en diseño de lecciones LEGO con metodología CEAEC."},
                {"role": "user", "content": prompt_usuario},
            ],
            max_output_tokens=3000,
        )
    except Exception as e:
        print("❌ Error al llamar a la API de OpenAI:", repr(e))
        return ""

    # Extraer el texto del objeto 'responses'
    texto_salida = ""
    for item in respuesta.output:
        for bloque in item.content:
            if getattr(bloque, "type", "") == "output_text":
                texto_salida += bloque.text

    return texto_salida


def main():
    # 1) Cargar variables de entorno desde .env
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("⚠️ No se encontró OPENAI_API_KEY en el archivo .env")
        return

    client = OpenAI(api_key=api_key)
    print("✅ Entorno listo. OPENAI_API_KEY detectada.")

    # 2) Leer el archivo de instrucciones LEGO
    instrucciones = cargar_instrucciones()
    print("✅ Instrucciones_LEGO.txt leído correctamente.")
    print("\n" + "=" * 60 + "\n")

    # 3) Leer el PDF de la lección modelo
    texto_pdf = leer_pdf_modelo()
    print("✅ PDF TS_WeDo_L01.pdf leído correctamente.")

    # 4) Leer las lecciones desde el Excel
    lecciones = leer_lecciones_desde_excel("Ejemplo.xlsx")
    print(f"✅ Excel leído correctamente. Se encontraron {len(lecciones)} lección(es).")
    print("\n" + "=" * 60)

    # 5) Generar una lección CEAEC por cada fila del Excel
    for datos_leccion in lecciones:
        leccion_num = datos_leccion.get("Lección", "")
        identificador = datos_leccion.get(
            "Identificador",
            f"L{int(leccion_num):02}" if leccion_num != "" else "LXX"
        )
        titulo_leccion = datos_leccion.get("Título de la lección", "Sin_título")

        print(f"🚀 Generando lección CEAEC para la lección {leccion_num}: {titulo_leccion}...")

        leccion_completa = generar_leccion_ceaec(instrucciones, texto_pdf, datos_leccion, client)

        if not leccion_completa.strip():
            print("⚠️ La lección generada está vacía. No se guardará archivo.")
            continue

        # Crear un nombre de archivo razonable, usando el identificador si existe
        nombre_base = identificador if identificador else f"L{leccion_num}"
        nombre_archivo_salida = f"{nombre_base}_CEAEC.md"

        with open(nombre_archivo_salida, "w", encoding="utf-8") as f:
            f.write(leccion_completa)

        print(f"   ✅ Lección generada y guardada en: {nombre_archivo_salida}")

    print("\n🎉 Proceso terminado. Revisa los archivos .md generados.")


if __name__ == "__main__":
    main()
