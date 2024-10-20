import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.comment_controller import router as comment_router
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()
# Inicializamos la aplicación FastAPI
app = FastAPI()

# Incluir el router de comentarios
app.include_router(comment_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes (usar con precaución en producción)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todas las cabeceras
)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("main:app", port=port, reload=True)