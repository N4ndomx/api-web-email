def styel_email_html(name:str,comentario:str):
    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                padding: 20px;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                color: #333333;
                font-size: 24px;
            }}
            p {{
                color: #555555;
                font-size: 19px;
            }}
            .comment {{
                font-style: italic;
                color: #666666;
                border-left: 4px solid #ff9800;
                padding-left: 10px;
                margin-top: 20px;
            }}
            .footer {{
                text-align: center;
                color: #888888;
                font-size: 12px;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>¡Hola {name}!</h1>
            <p>Agradecemos tu sugerencia :</p>
            <div class="comment">
                <p>{comentario}</p>
            </div>
            <p>Te aseguramos que lo tendremos en cuenta para el desarrollo de nuestra plataforma.</p>
            <br>
            <div class="footer">
                <p>Este correo ha sido generado automáticamente. No responda a este mensaje.</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content
