
class MockPerson:

    @classmethod
    def fields(cls):

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
