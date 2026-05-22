# ProcessDoc AI

AI-powered tool for automatic process documentation – enter a process, get structured documentation.

## Features
- Generate structured process documentation via Gemini AI
- Download documentation as PDF or DOCX
- Save and view documentation history
- Error handling for empty inputs

The documentation can be downloaded directly as a PDF.

## Tech Stack

- **Backend:** Python, Flask
- **AI:** Google Gemini API
- **Database:** SQLite
- **Export:** ReportLab (PDF), python-docx (DOCX)
- **Frontend:** HTML, CSS, JavaScript

## Installation

```bash
# Clone repository
git clone https://github.com/Luanhsn/ProcessDocAI.git
cd ProcessDocAI

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install flask google-genai python-dotenv markdown reportlab

# Create .env file
echo "GEMINI_API_KEY=your_key_here" > .env

# Start app
python app.py
```

Then open your browser at: `http://localhost:5000`

## Gemini API Key

Get a free API key at: [aistudio.google.com](https://aistudio.google.com)

## Project Structure

```
ProcessDocAI/
├── app.py # Flask backend + Gemini integration
├── dokumentationen.db # SQLite database
├── .env # API key
├── .gitignore
└── templates/
├── index.html # Main page
└── history.html # Documentation history
```

## Usage
1. Enter a process name in the input field
2. Click "Dokumentation erstellen"
3. Download the result as PDF or DOCX
4. View previous documentation under "Verlauf""
