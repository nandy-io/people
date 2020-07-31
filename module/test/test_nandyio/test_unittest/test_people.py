import unittest
import unittest.mock

import nandyio.unittest.people


class TestMockPerson(unittest.TestCase):

    def test_fields(self):

        self.assertEqual(nandyio.unittest.people.MockPerson.fields(), [{
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
        }])

    def test_model(self):

        self.assertEqual(nandyio.unittest.people.MockPerson.model(id=1), {
            "id": 1,
            "name": "unit"
        })

        self.assertEqual(nandyio.unittest.people.MockPerson.model(name="unit"), {
            "id": 1,
            "name": "unit"
        })

        self.assertEqual(nandyio.unittest.people.MockPerson.model(id=2), {
            "id": 2,
            "name": "test"
        })

        self.assertEqual(nandyio.unittest.people.MockPerson.model(name="test"), {
            "id": 2,
            "name": "test"
        })