# Expense Tracker

A command-line and web-based expense tracker built in Python. Add, view, and delete personal expenses, with automatic total calculation and persistent storage using JSON.

## Features
- Add expenses with description, amount, and category
- View all recorded expenses
- Delete individual expenses
- Automatic running total
- Data persists between sessions (saved to `data.json`)
- Two interfaces: command-line menu (`expense_tracker.py`) and a Flask web app (`app.py`)

## Running the CLI version
```
python3 expense_tracker.py
```

## Running the web version
```
python3 app.py
```
Then open `http://127.0.0.1:5000` in your browser.

## Built with
- Python 3
- Flask
- JSON for data storage
- pytest for testing