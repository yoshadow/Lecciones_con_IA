# main.py
import os
import base64
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


def cargar_imagen_base64(ruta_imagen: Path) -> str:
    """
    Carga una imagen y la devuelve como string base64 tipo data URL,
    lista para usar con la API de OpenAI (input_image).
    """
    if not ruta_imagen.exists():
        raise FileNotFoundError(f"No se encontró la imagen: {ruta_imagen}")

    with ruta_imagen.open("rb") as img:
        b64 = base64.b64encode(img.read()).decode("utf-8")

    # Detectar tipo MIME simple por extensión
    ext = ruta_imagen.suffix.lower()
    if ext in [".jpg", ".jpeg"]:
        mime = "image/jpeg"
    elif ext == ".png":
        mime = "image/png"
    else:
        # por defecto
        mime = "image/png"

    return f"data:{mime};base64,{b64}"


def leer_lecciones_desde_excel(nombre_archivo: str = "Tabla.xlsx") -> list[dict]:
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


def generar_leccion_ceaec(instrucciones: str, texto_pdf: str, datos: dict, client: OpenAI, imagen_exploro_dataurl: str | None = None,) -> str:
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
    fragmento_pdf = texto_pdf[:3000]

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

Genera una lección completa siguiendo EXACTAMENTE las etapas de la metodología CEAEC.
Desarrolla todas las etapas como si estuvieran escritas en un LIBRO DEL ALUMNO.

La ACTIVIDAD 1 de la etapa EXPLORO debe basarse específicamente en el programa/proyecto que aparece en la imagen adjunta.

Incluye al inicio:

Una TABLA INICIAL con:
 - Número de lección
 - Título de la lección
 - Identificador
 - Nivel
 - Objetivo
 - Habilidades
 - Materiales
 - Recursos digitales

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

Estilo general similar al siguiente fragmento del PDF:

\"\"\"{fragmento_pdf}\"\"\"
"""
    # Contenido combinado: texto + (opcional) imagen
    contenido_usuario = [
        {"type": "input_text", "text": prompt_usuario},
    ]

    if imagen_exploro_dataurl:
        contenido_usuario.append(
            {
                "type": "input_image",
                "image_url": imagen_exploro_dataurl,
            }
        )

    try:
        respuesta = client.responses.create(
            model="gpt-5.1",
            instructions="Eres un experto en diseño de lecciones LEGO con metodología CEAEC.",
            input=[
                {
                    "role": "user",
                    "content": contenido_usuario,
                }
            ],
            max_output_tokens=3000,
        )
    except Exception as e:
        print("❌ Error al llamar a la API de OpenAI:", repr(e))
        return ""

    # Atajo del SDK: todo el texto junto
    return respuesta.output_text or ""


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
    print("✅ PDF leído correctamente.")

    # 4) Leer las lecciones desde el Excel
    lecciones = leer_lecciones_desde_excel("Tabla.xlsx")
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

        # Leer el nombre de la imagen desde el Excel (columna "Imagen exploro")
        nombre_imagen = (datos_leccion.get("Imagen exploro") or datos_leccion.get("Imagen Exploro") or "")

        # Si hay nombre de imagen, la cargamos desde la carpeta /imagenes
        imagen_dataurl = None
        if nombre_imagen:
            ruta_img = Path(__file__).parent / "imagenes" / str(nombre_imagen)
            try:
                imagen_dataurl = cargar_imagen_base64(ruta_img)
            except FileNotFoundError as e:
                print(f"⚠️ {e}. Se generará la lección sin imagen para Exploro 1.")

        print(f"🚀 Generando lección CEAEC para la lección {leccion_num}: {titulo_leccion}...")

        # Aquí pasamos la imagen a la función (nuevo parámetro)
        leccion_completa = generar_leccion_ceaec(instrucciones, texto_pdf, datos_leccion, client, imagen_exploro_dataurl=imagen_dataurl,)

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
