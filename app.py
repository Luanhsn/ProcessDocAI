from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():

    prozess = request.form.get("prozess_name")

    prompt = f"""
       Erstelle eine strukturierte Prozessdokumentation für: {prozess}

       Bitte gliedere sie so:
       1. Ziel des Prozesses
       2. Schritte (nummeriert)
       3. Verantwortliche pro Schritt
       4. Checkliste am Ende
       """

    response = model.generate_content(prompt)
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return render_template("index.html", result=response.text)


if __name__ == "__main__":
    app.run(debug=True)