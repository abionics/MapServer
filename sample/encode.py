import base64
import pickle

from urllib.parse import quote_plus

url = 'https://example.com/map?points='
# url = 'http://127.0.0.1:8000/map?points='

points = [
    {
        'coords': [50.541373, 30.589153],
        'text': 'Some text 1',
    },
    {
        'coords': [50.432992, 30.622825],
        'text': 'Some text 2',
        'circle': {
            'radius': 3000,
        },
    },
    {
        'coords': [50.448646, 30.448171],
        'text': 'Some text 3',
        'circle': {
            'radius': 3000,
            'inner_radius': 2000,
            'color': '#00FF00',
            'opacity': 0.5,
        },
    },
]

dump = pickle.dumps(points)
encoded = base64.b64encode(dump).decode()
param = quote_plus(encoded)
print(url + param)
