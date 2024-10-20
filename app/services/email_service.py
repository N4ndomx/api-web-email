import os
import smtplib
from email.message import EmailMessage
from app.models.comment_model import Comment
# Servicio para enviar correos electrónicos
def send_email(to_email: str, data: Comment, mock:str):
    from_email = os.getenv("EMAIL_USERNAME")
    from_password = os.getenv("EMAIL_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))

    subject = "Gracias por su Comentario"

    
    # Crear el contenido del correo
    msg = EmailMessage()
    msg.set_content(f"Has recibido un nuevo comentario: {data.comment}")
    msg.add_alternative(mock, subtype='html')  # Contenido HTML
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Enviar el correo
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
            smtp.login(from_email, from_password)
            smtp.send_message(msg)
        return True
    except Exception as e:
        print(f"Error enviando el correo: {e}")
        return False
