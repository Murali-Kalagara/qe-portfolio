@echo off
REM ============================
REM QE Portfolio - Task Runner
REM ============================

REM Activate virtual environment
call .venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Run linter (ruff)
ruff check .

REM Format code (black)
black .

REM Run tests quietly
pytest -q

REM Deactivate virtual environment
deactivate

echo.
echo All tasks completed!
pause