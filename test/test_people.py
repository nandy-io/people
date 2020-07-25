import unittest
import unittest.mock

import nandyio.people
import nandyio.unittest.people


class TestPerson(unittest.TestCase):

    @unittest.mock.patch("requests.options")
    def test_fields(self, mock_options):

        def options(url, params=None):

            response = unittest.mock.MagicMock()

            if url == "http://api.people-nandy-io/integrate":

                response.json.return_value = {
                    "options": [
                        1,
                        2
                    ],
                    "labels": {
                        1: "unit",
                        2: "test"
                    }
                }

            return response

        mock_options.side_effect = options

        self.assertEqual(nandyio.people.Person.fields(), [{
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

    @unittest.mock.patch("requests.get")
    def test_model(self, mock_get):

        def get(url, params=None):

            response = unittest.mock.MagicMock()

            if (
                url == "http://api.people-nandy-io/person/1" or
                (url == "http://api.people-nandy-io/integrate" and params["name"] == "unit")
            ):

                response.json.return_value = {
                    "person": {
                        "id": 1,
                        "name": "unit"
                    }
                }

            elif (
                url == "http://api.people-nandy-io/person/2" or
                (url == "http://api.people-nandy-io/integrate" and params["name"] == "test")
            ):

                response.json.return_value = {
                    "person": {
                        "id": 2,
                        "name": "test"
                    }
                }

            return response

        mock_get.side_effect = get

        self.assertEqual(nandyio.people.Person.model(id=1), {
            "id": 1,
            "name": "unit"
        })

        self.assertEqual(nandyio.people.Person.model(name="unit"), {
            "id": 1,
            "name": "unit"
        })

        self.assertEqual(nandyio.people.Person.model(id=2), {
            "id": 2,
            "name": "test"
        })

        self.assertEqual(nandyio.people.Person.model(name="test"), {
            "id": 2,
            "name": "test"
        })

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