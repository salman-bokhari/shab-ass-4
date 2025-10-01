# Professional Calculator CLI

Command-line calculator application in Python with 100% test coverage (configured).
Includes:
- REPL interface (app/calculator/cli.py)
- Modular operations (app/operation)
- Calculation and factory (app/calculation)
- Unit tests using pytest
- GitHub Actions workflow to run tests and enforce coverage

## Setup (local)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=. pytest --cov=app tests/
```

## Usage
Run the REPL:
```bash
python run.py
```

Commands inside REPL:
- `add`, `sub`, `mul`, `div` (or `+`, `-`, `*`, `/`)
- `history` - show past calculations
- `help` - show help
- `exit` - quit

## Notes
The GitHub Actions workflow enforces 100% coverage. Lines intentionally excluded from coverage use `# pragma: no cover`.
