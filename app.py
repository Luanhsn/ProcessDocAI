from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")


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

    return render_template("index.html", result=response.text)


if __name__ == "__main__":
    app.run(debug=True)