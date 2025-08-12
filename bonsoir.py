from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        with open("bonsoir.txt", "r", encoding="utf-8") as f:
            contenu = f.read()
    except Exception as e:
        contenu = f"Erreur lors de la lecture du fichier : {e}"

    return f"""
    <html>
    <head><title>Bonsoir</title></head>
    <body>
        <h1>{contenu}</h1>
        <img src="/static/severin.jpg" alt="Severin" style="max-width:500px;">
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
