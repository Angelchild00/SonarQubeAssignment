# Calculator (SonarQube Cloud practice project)

A small Python calculator used for CSCN73010 Assignment 3: static code analysis
with SonarQube Cloud through GitHub Actions.

- **Language:** Python 3.12
- **Test framework:** pytest, with coverage from pytest-cov
- **CI:** GitHub Actions (`.github/workflows/sonarcloud.yml`)

## Run locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest --cov=src --cov-report=term
```

Run the interactive calculator:

```bash
python src/calculator/cli.py
```
