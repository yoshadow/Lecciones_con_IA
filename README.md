# Lecciones con IA

Generador automatizado de planes de clase utilizando el modelo de inteligencia artificial Open AI.
Aunque originalmente está configurado para generar lecciones de robótica educativa con LEGO WeDo 2.0, el sistema puede adaptarse fácilmente para generar contenido educativo de cualquier materia o disciplina mediante la modificación de instrucciones y datos de entrada.

---

## Características principales

- Generación automatizada de lecciones completas siguiendo una metodología definida.
- Lectura de datos desde archivos Excel para configurar múltiples lecciones.
- Uso de archivos PDF como referencia de estilo y estructura.
- Inclusión opcional de imágenes o capturas de pantalla como apoyo dentro de las lecciones.
- Exportación de cada lección generada en formato Markdown.
- Personalizable para cualquier área educativa mediante edición de reglas en el archivo de instrucciones.

---

## Flujo de trabajo

1. Colocar un archivo PDF modelo dentro de la carpeta `pdfs`, el cual sirve como referencia de estilo.
2. Completar el archivo Excel `Ejemplo.xlsx` con la información de las lecciones que se desean generar.
3. Ajustar las reglas de generación en el archivo `Instrucciones_LEGO.txt`.
4. Ejecutar el archivo principal:

```
python main.py
```

5. Los archivos `.md` generados se guardarán en la carpeta raíz del proyecto.

---

## Requisitos

- Python 3.10 o superior.
- Clave de API de OpenAI.
- Archivo `.env` configurado con:

```
OPENAI_API_KEY=tu_clave_de_api
```

- Instalar dependencias con:

```
pip install -r requirements.txt
```

---

## Estructura del archivo Excel

El archivo debe contener las siguientes columnas a partir de la segunda fila:

| Columna                     | Descripción                                                       |
|-----------------------------|-------------------------------------------------------------------|
| Lección                    | Número o identificador numérico de la lección                     |
| Título de la lección       | Nombre o título de la lección                                     |
| Identificador              | Código único de la lección                                         |
| Área de contenido          | Disciplina o área educativa correspondiente                        |
| Tema                       | Tema general que aborda la lección                                 |
| Recursos digitales         | Herramientas o software utilizados                                 |
| Materiales                 | Lista de materiales requeridos                                      |
| Contenidos                 | Conceptos clave incluidos en la lección                            |
| Objetivos de aprendizaje   | Objetivos principales que se buscan alcanzar                       |
| Habilidades                | Habilidades a desarrollar                                           |
| Competencia STEAM          | Competencias relacionadas                                          |
| Actividad de exploración   | Actividad inicial para introducir el tema                          |
| Actividad complementaria   | Actividad de extensión o profundización                            |
| Imagen exploro (opcional)  | Nombre de una imagen que se utilizará en la sección correspondiente |

---

## Personalización para otras materias

Este proyecto no está limitado a robótica ni a LEGO. Puede adaptarse a materias como:

| Área               | Aplicación                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| Ciencias Naturales | Generar prácticas de laboratorio o actividades experimentales               |
| Matemáticas        | Crear lecciones basadas en problemas, ejercicios o demostraciones           |
| Historia           | Diseñar actividades a partir de líneas del tiempo, mapas o fuentes históricas|
| Arte               | Generar análisis, actividades de apreciación o proyectos creativos          |
| Lenguaje           | Crear lecturas guiadas, ejercicios de escritura o comprensión lectora       |

Para lograr esto, basta con:

- Modificar el archivo `Instrucciones_LEGO.txt`.
- Proporcionar un PDF de referencia adecuado.
- Ajustar la estructura del Excel para incluir campos relevantes.

---

## Metodología

El contenido generado se basa en la plantilla que se encuentra en el archivo `Instrucciones_LEGO.txt`.
Puedes editar libremente este archivo para:

- Cambiar la metodología.
- Cambiar el tono de escritura.
- Ajustar reglas de contenido.
- Crear nuevas secciones personalizadas.

---

## Ejecución

Para correr el proyecto:

```
python main.py
```

El sistema procesará cada fila del archivo Excel y generará un archivo Markdown por cada lección.

---

## Contribuciones

Cualquier colaborador puede apoyar con:

- Nuevas plantillas metodológicas.
- Nuevos formatos de entrada (como Google Sheets o bases de datos).
- Mejoras al prompt o estructura del código.
- Automatización de imágenes.
- Integración con APIs externas.

Se aceptan PRs y sugerencias.

---

## Licencia

Este proyecto se distribuye bajo la licencia MIT.
El uso del sistema y sus adaptaciones es completamente libre con atribución al autor original.
