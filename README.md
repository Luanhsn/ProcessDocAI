# ProcessDoc AI

AI-powered tool for automatic process documentation – enter a process, get structured documentation.

## What it does

The user enters a process in plain language – e.g. "New Employee Onboarding". The app sends it to the Gemini API and returns structured documentation including:

- Goal of the process
- Numbered steps
- Responsible parties per step
- Checklist

The documentation can be downloaded directly as a PDF.

## Tech Stack

- Python
- Flask
- Google Gemini API
- ReportLab (PDF generation)
- python-markdown

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
├── app.py              # Flask backend + Gemini integration
├── .env                # API key (not included in repository)
├── .gitignore
└── templates/
    └── index.html      # Frontend
```

## Example Inputs

- "New Employee Onboarding"
- "Invoice approval process"
- "Software deployment to all devices"
- "IT incident reporting and resolution"
