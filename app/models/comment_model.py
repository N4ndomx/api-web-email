from pydantic import BaseModel, EmailStr

# Definir el modelo de datos para un comentario
class Comment(BaseModel):
    name:str
    last_names:str
    email: EmailStr
    comment: str
