from fastapi import APIRouter, HTTPException
from app.services.mockups_email_html.comentario_user import styel_email_html
from app.models.comment_model import Comment
from app.services.email_service import send_email

# Crear el enrutador para los comentarios
router = APIRouter()

# Endpoint para recibir el comentario y enviar el correo
@router.post("/comentarios/")
async def receive_comment(comment: Comment):
    success = send_email(comment.email, comment, styel_email_html(comment.name +' '+ comment.last_names,comment.comment))

    if success:
        return {"message": f"Comentario enviado correctamente al correo {comment.email}"}
    else:
        raise HTTPException(status_code=500, detail="Error enviando el correo")
