# ProcessDoc AI

KI-gestütztes Tool zur automatischen Prozessdokumentation – Prozess eingeben, strukturierte Dokumentation erhalten.

## Was es macht

Der User gibt einen Prozess in einfachen Worten ein – z.B. "Neuer Mitarbeiter Onboarding". Die App schickt das an die Gemini API und gibt eine strukturierte Dokumentation zurück mit:

- Ziel des Prozesses
- Nummerierte Schritte
- Verantwortliche pro Schritt
- Checkliste

Die Dokumentation kann direkt als PDF heruntergeladen werden.

## Tech Stack

- Python
- Flask
- Google Gemini API
- ReportLab (PDF-Generierung)
- python-markdown
