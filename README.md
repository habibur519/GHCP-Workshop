# Rock Paper Scissors Lizard Spock

A Python implementation of the extended Rock-Paper-Scissors-Lizard-Spock game.

This project includes:

- a command-line game interface in `main.py`
- a Flask-based REST API in `app.py`
- a browser UI served from `/`
- reusable game logic and helper functions
- unit tests for game behavior and API endpoints

## Purpose

The goal of this repository is to provide a small game service that can be played in multiple ways:

- interactive CLI play in the terminal
- REST API requests for automation and clients
- browser-based UI for easy browser play

It also demonstrates how to separate game logic from input/output and support both command-line and web application usage.

## Project Structure

- `main.py` - game logic and command-line interface
- `app.py` - Flask app exposing the REST API and browser UI
- `templates/index.html` - browser-based UI for selecting and playing choices
- `test_main.py` - unit tests for game logic
- `test_api.py` - API tests for Flask endpoints
- `requirements.txt` - project dependencies

## Running locally

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Run the command-line game

```bash
python main.py
```

Then enter one of: `rock`, `paper`, `scissors`, `lizard`, or `spock`.

### Run the REST API and browser UI

```bash
python app.py
```

Open the UI in a browser:

```text
http://127.0.0.1:5000/
```

### REST API examples

```bash
curl -X POST http://127.0.0.1:5000/rock
curl -X POST http://127.0.0.1:5000/play -H "Content-Type: application/json" -d '{"choice": "spock"}'
```

### API response format

The API returns JSON with:

- `user_choice`
- `computer_choice`
- `result` (`tie`, `user`, or `computer`)

## Testing

```bash
python -m pytest -q
```

## Notes

- The browser UI uses the `/play` endpoint under the hood.
- The game logic is reusable and separate from Flask and CLI code.
- `requirements.txt` currently includes `Flask` and `pytest`.

## License

This project is provided as-is for experimentation and learning.
