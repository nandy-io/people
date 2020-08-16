"""
Module for adding Person integrations to other Models
"""

import copy
import requests
import klotio
import klotio_sqlalchemy_restful

class Person(klotio_sqlalchemy_restful.Model):
    """
    Person integration Model class
    """

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
        """
        Returns fields for this integration
        """

        return [klotio.integrate(copy.deepcopy(cls.FIELD))]

    @staticmethod
    def model(id=None, name=None):
        """
        Looks up model by id or name
        """

        if id:
            return requests.get(f"http://api.people-nandy-io/person/{id}").json()["person"]
        elif name:
            return requests.get("http://api.people-nandy-io/integrate", params={"name": name}).json()["person"]

        return None
