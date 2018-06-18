import os
import json
from collections import OrderedDict

_location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(_location, 'data.json')) as f:
    fixtures = json.load(f, object_pairs_hook=OrderedDict)
