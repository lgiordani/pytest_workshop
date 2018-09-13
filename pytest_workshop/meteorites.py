import urllib.request
import json

from pytest_workshop import calc

URL = ("https://raw.githubusercontent.com/lgiordani/"
       "pytest_workshop/master/earth-meteorite-landings.json")


class MeteoriteStats:
    def get_data(self):
        with urllib.request.urlopen(URL) as url:
            return json.loads(url.read().decode())

    def average_mass(self, data):
        c = calc.Calc()
        masses = [float(d['mass']) for d in data if 'mass' in d]

        return c.avg(masses)
