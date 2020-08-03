import copy
import requests
import klotio.service

class Person(klotio.service.Model):

    FIELD = {
        "name": "person_id",
        "label": "person",
        "style": "radios",
        "integrate": {
            "url": "http://api.people-nandy-io/integrate"
        }
    }

    @classmethod
    def fields(cls):

        return [cls.integrate(copy.deepcopy(cls.FIELD))]

    @staticmethod
    def model(id=None, name=None):

        if id:
            return requests.get(f"http://api.people-nandy-io/person/{id}").json()["person"]
        elif name:
            return requests.get(f"http://api.people-nandy-io/integrate", params={"name": name}).json()["person"]