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
    <head>
        <title>Bonsoir Chic</title>
        <style>
            body {{
                font-family: 'Segoe UI', sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                padding: 50px;
            }}
            .card {{
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                display: inline-block;
            }}
            img {{
                max-width: 400px;
                margin: 20px 0;
                border-radius: 8px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>{contenu}</h1>
            <img src="/static/severin.jpg" alt="Severin">
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=po
