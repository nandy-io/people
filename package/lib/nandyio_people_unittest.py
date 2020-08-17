"""
Moduule for making unittesting easier with Person
"""

class MockPerson:
    """
    Mock class for Person. Patch with it.
    Has two people unit and test with ids 1 and 2
    """

    @classmethod
    def fields(cls):
        """
        Returns fields with two people
        """

        return [{
            "name": "person_id",
            "label": "person",
            "style": "radios",
            "integrate": {
                "url": "http://api.people-nandy-io/integrate"
            },
            "options": [
                1,
                2
            ],
            "labels": {
                1: "unit",
                2: "test"
            }
        }]

    @staticmethod
    def model(id=None, name=None):
        """
        Looks up the model for unit or test, ny name or id
        """

        if id == 1 or name == "unit":
            return {
                "id": 1,
                "name": "unit"
            }
        elif id == 2 or name == "test":
            return {
                "id": 2,
                "name": "test"
            }

        return None
