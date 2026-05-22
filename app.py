import re
from io import BytesIO
from flask import Flask, render_template, request, send_file
from google import genai
from dotenv import load_dotenv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from docx import Document
import os
import markdown
import sqlite3

app = Flask(__name__)

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def init_db():
    conn = sqlite3.connect("dokumentationen.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dokumentationen (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            inhalt TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def clean_for_html(content):
    return markdown.markdown(content, extensions=["tables"])
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():

    process = request.form.get("prozess_name")

    if not process:
        return render_template("index.html", error="Es muss etwas eingegeben werden")

    prompt = f"""
       Erstelle eine strukturierte Prozessdokumentation für: {process}

       Bitte gliedere sie so:
       1. Ziel des Prozesses
       2. Schritte (nummeriert)
       3. Verantwortliche pro Schritt
       4. 4. Checkliste am Ende (als normale nummerierte Liste, keine Checkboxen, keine Klammern)
       """

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    result_text = response.text

    conn = sqlite3.connect("dokumentationen.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dokumentationen (inhalt) VALUES (?)", (result_text,))
    conn.commit()
    conn.close()

    result_html = markdown.markdown(response.text, extensions=["tables"])

    return render_template("index.html", result=result_html, result_text=result_text)


@app.route("/pdf_download", methods=["POST"])
def file_download():
    content = request.form.get("content")
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    content = content.replace('\r\n', '\n').replace('\r', '\n')
    content = re.sub(r'#{1,6}\s*', '', content)
    content = re.sub(r'\*\*(.*?)\*\*', r'\1', content)
    content = re.sub(r'\*', '', content)

    width, height = A4
    y = height - 50

    for line in content.split("\n"):
        if y < 50:
            p.showPage()
            y = height - 50
        p.drawString(50, y, line)
        y -= 20

    p.save()
    buffer.seek(0)

    return send_file(
        buffer,
        mimetype="application/pdf",
        as_attachment=True,
        download_name="dokumentation.pdf"
    )

@app.route("/docx_download", methods=["POST"])
def docx_download():
    content = request.form.get("content")
    doc = Document()

    content = content.replace('\r\n', '\n').replace('\r', '\n')

    for line in content.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("# "):
            doc.add_heading(line[2:], level=1)
        elif line.startswith("## "):
            doc.add_heading(line[3:], level=2)
        elif line.startswith("### "):
            doc.add_heading(line[4:], level=3)
        else:
            line = re.sub(r'\*\*(.*?)\*\*', r'\1', line)
            line = re.sub(r'\*', '', line)
            doc.add_paragraph(line)

    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    return send_file(
        buffer,
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        as_attachment=True,
        download_name="dokumentation.docx"
    )

@app.route("/history")
def verlauf():
    conn = sqlite3.connect("dokumentationen.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dokumentationen")
    entries = cursor.fetchall()
    conn.close()
    return render_template("history.html", entries=entries)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)