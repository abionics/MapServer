import base64
import pickle
from urllib.parse import quote_plus

from colour import Color

url = 'http://127.0.0.1:8000/map?points='

red = Color('red')
colors = red.range_to(Color('blue'), 4)
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
            'color': next(colors).hex_l,
        },
    },
    {
        'coords': [50.448646, 30.448171],
        'text': 'Some text 3',
        'circle': {
            'radius': 3000,
            'inner_radius': 2000,
            'color': next(colors).hex_l,
            'opacity': 0.5,
        },
    },
    {
        'coords': [50.132992, 30.222825],
        'text': 'Some text 4',
        'circle': {
            'radius': 3000,
            'color': next(colors).hex_l,
        },
    },
    {
        'coords': [50.932992, 30.922825],
        'text': 'Some text 5',
        'circle': {
            'radius': 3000,
            'color': next(colors).hex_l,
        },
    },
]

dump = pickle.dumps(points)
encoded = base64.b64encode(dump).decode()
param = quote_plus(encoded)
print(url + param)
