import base64
import json
import os
import pickle

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

TEMPLATE_FILE = os.getenv('TEMPLATE_FILE', 'template.html')
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')


@app.get('/map', response_class=HTMLResponse)
async def map(points: str) -> str:
    points = _decode(points)
    points_str = json.dumps(points)
    content = _load_file(TEMPLATE_FILE)
    return content \
        .replace('{GOOGLE_MAPS_API_KEY}', GOOGLE_MAPS_API_KEY) \
        .replace('{POINTS}', points_str)


def _decode(points: str) -> dict:
    dump = base64.b64decode(points)
    return pickle.loads(dump)


def _load_file(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()
