import os
import json

_location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(_location, 'small.json')) as f:
    fixtures = json.load(f)

with open(os.path.join(_location, '1000.json')) as f:
    fixtures['1000'] = json.load(f)
