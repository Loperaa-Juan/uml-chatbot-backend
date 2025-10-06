from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from diagram import create_diagram

app = FastAPI(
    title="UML Diagram Generator API",
    description="API para generar código PlantUML a partir de descripciones de arquitectura.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes (ideal para desarrollo)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class DiagramRequest(BaseModel):
    requisito: str

@app.post('/uml', response_model=str)
def get_diagram(request: DiagramRequest):
    """
    Recibe una descripción de la arquitectura y devuelve el código PlantUML correspondiente.
    """
    response = create_diagram(requisito=request.requisito)
    return response
