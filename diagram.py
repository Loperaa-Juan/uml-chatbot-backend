import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_APIKEY"))


def create_diagram(requisito: str):
    instruction = """
    res un experto en arquitectura de software, DevOps y modelado UML. 
Genera código **PlantUML** para **diagramas de despliegue (Deployment Diagrams)** claros, completos y coherentes.

⚙️ Instrucciones:
- Responde solo con el bloque `@startuml ... @enduml`.
- No agregues texto ni explicaciones fuera del bloque.
- Usa nombres descriptivos y una estructura ordenada.

🏗️ Estructura esperada:
1. `title` con el nombre del sistema.
2. Nodos (`node`) con estereotipos como `<<client>>`, `<<server>>`, `<<database>>`, `<<cloud>>`, `<<container>>`.
3. Artefactos (`artifact` o `component`) dentro de los nodos para detallar servicios o módulos.
4. Conexiones (`-->`) con protocolo o tipo de comunicación (HTTPS, SQL, MQTT, etc.).
5. Elementos opcionales: balanceadores, colas, cache, autenticación, servicios externos o cloud.
6. Si la descripción es ambigua, asume una arquitectura web moderna (frontend, backend, base de datos, cloud).

    """

    try:
        response = client.responses.create(
            model="gpt-5",
            input=f"{instruction}, el requisito es: {requisito}"
        )
        
        return response.output_text
    except Exception as e:
        print(f"Error al llamar a la API de OpenAI: {e}")
        return
