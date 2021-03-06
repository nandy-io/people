import unittest
import unittest.mock
import klotio_unittest

import nandyio_people_integrations
import nandyio_people_unittest


class TestMockPerson(klotio_unittest.TestCase):

    @unittest.mock.patch("nandyio_people_integrations.Person", nandyio_people_unittest.MockPerson)
    def test_fields(self):

        self.assertEqual(nandyio_people_integrations.Person.fields(), [{
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

    @unittest.mock.patch("nandyio_people_integrations.Person", nandyio_people_unittest.MockPerson)
    def test_model(self):

        self.assertEqual(nandyio_people_integrations.Person.model(id=1), {
            "id": 1,
            "name": "unit"
        })

        self.assertEqual(nandyio_people_integrations.Person.model(name="unit"), {
            "id": 1,
            "name": "unit"
        })

        self.assertEqual(nandyio_people_integrations.Person.model(id=2), {
            "id": 2,
            "name": "test"
        })

        self.assertEqual(nandyio_people_integrations.Person.model(name="test"), {
            "id": 2,
            "name": "test"
        })

        self.assertIsNone(nandyio_people_integrations.Person.model(0))
