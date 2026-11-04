# Programmering2Grupp

## Om projektet

En webbapplikation som visualiserar historiska drivmedelspriser i Sverige mellan 2021 och 2026.

### Funktioner
- Visualisering av bensin (E95) och dieselpriser.
- Visar historiska högsta och lägsta priser.
- Jämför priser mellan två valda datum.
- Presenterar prisutvecklingen med diagram och text.
- Navigering mellan olika vyer och endpoints.

## Tekniker
- Python 3.10+
- Flask
- Pandas
- Plotly
- Jinja2
- Pytest

## Installation

### 1. Ladda ner projektet

Klona repository:

```bash
git clone <repository-url>
cd Programmering2Grupp
```

Alternativt kan du ladda ner projektet som ZIP via GitHubs **Code → Download ZIP** och extrahera filerna.

### 2. Skapa en virtuell miljö

**Windows:**
```bash
py -3 -m venv venv
```

**macOS / Linux:**
```bash
python3 -m venv venv
```

### 3. Aktivera miljön

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 4. Installera beroenden

Kör följande kommandon i projektets rotmapp:

```bash
python -m pip install -r requirements.dev.txt
python -m pip install -r requirements.txt
```

### 5. Starta applikationen

```bash
flask run
```

Öppna sedan http://127.0.0.1:5000 i webbläsaren.

För att avsluta applikationen, tryck `Ctrl + C` i terminalen.

Avsluta den virtuella miljön med:

```bash
deactivate
```

## Köra tester

Aktivera den virtuella miljön och kör:

```bash
pytest
```

Pytest hittar och kör automatiskt projektets tester.

- **PASSED:** Testet har godkänts.
- **FAILED:** Testet har misslyckats. Pytest visar information om felet.

Du behöver inte starta Flask-applikationen separat för att köra testerna, förutsatt att testerna använder Flask:s testklient.

## API och datakällor

Projektet använder [fuel-prices.eu API](https://www.fuel-prices.eu/api/docs/) för att hämta historiska drivmedelspriser.

Priserna hämtas i EUR och omvandlas till SEK i applikationen.

### Källhänvisning och licens

Historiska data från EU Weekly Oil Bulletin och fuel-prices.eu:s bearbetade data omfattas av [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), enligt respektive datakällas licensvillkor.

**Attribution:**

Source: European Commission, EU Weekly Oil Bulletin, processed by [fuel-prices.eu](https://www.fuel-prices.eu/).

Mer information:
- [API-dokumentation](https://www.fuel-prices.eu/api/docs/)
- [Licensvillkor](https://www.fuel-prices.eu/license/)
- [Datakällor och licenser](https://www.fuel-prices.eu/sources/)

Observera att olika datakällor kan ha separata licensvillkor. Applikationen är ett självständigt studentprojekt och är inte officiellt kopplad till eller godkänd av fuel-prices.eu eller Europeiska kommissionen.

## Tack för du använder vår app!

![<3](https://w7.pngwing.com/pngs/150/440/png-transparent-meme-culture-idea-saying-meme-culture-text-presentation-thumbnail.png)