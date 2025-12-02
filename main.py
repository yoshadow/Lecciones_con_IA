
# main.py
import os
from dotenv import load_dotenv

def main():
    # Cargar variables de entorno desde .env
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("⚠️ No se encontró OPENAI_API_KEY en el archivo .env")
    else:
        print("✅ Entorno listo. OPENAI_API_KEY detectada.")
        # Aquí después integraremos la lógica para leer el PDF y llamar a la API

if __name__ == "__main__":
    main()
