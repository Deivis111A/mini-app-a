import random
import string
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Generador de Contraseñas - Version A")

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head><title>Generador</title></head>
    <body>
        <h1>Generador de Contraseñas</h1>
        <form action="/generate-password" method="get">
            Longitud: <input type="number" name="length" value="10">
            <button type="submit">Generar</button>
        </form>
    </body>
    </html>
    """

@app.get("/generate-password")
def generate(length: int = 10):
    chars = string.ascii_letters + string.digits
    pwd = "".join(random.choice(chars) for _ in range(length))
    return {"password": pwd, "length": length}
