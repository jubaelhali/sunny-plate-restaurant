# Sunny Plate Restaurant

A responsive sample restaurant website built with HTML, CSS, JavaScript, and Python Flask.

## Run locally
1. Install Python.
2. Open a terminal in this project folder.
3. Run `pip install -r requirements.txt`.
4. Run `python app.py`.
5. Open `http://127.0.0.1:5000`.

## Deploy on Render
- Create a new **Web Service** and connect this GitHub repository.
- Root Directory: leave blank.
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

`requirements.txt` and `app.py` must be in the repository's top-level folder.

## Routes
- `/` - restaurant website
- `/api/menu` - menu data in JSON
- `/health` - health check

The order panel is a front-end sample only. It does not send real orders or accept payments.
