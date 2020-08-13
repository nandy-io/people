import unittest
import unittest.mock
import klotio_unittest
import test_models

import os
import json
import yaml

import flask
import opengui
import sqlalchemy.exc

import models
import service


class TestRestful(klotio_unittest.TestCase):

    maxDiff = None

    @classmethod
    @unittest.mock.patch("klotio.logger", klotio_unittest.MockLogger)
    def setUpClass(cls):

        cls.app = service.app()
        cls.api = cls.app.test_client()

    def setUp(self):

        self.app.mysql.drop_database()
        self.app.mysql.create_database()

        self.session = self.app.mysql.session()
        self.sample = test_models.Sample(self.session)

        self.app.mysql.Base.metadata.create_all(self.app.mysql.engine)

    def tearDown(self):

        self.session.close()
        self.app.mysql.drop_database()


class TestAPI(TestRestful):

    @unittest.mock.patch("klotio.logger", klotio_unittest.MockLogger)
    def test_app(self):

        app = service.app()

        self.assertEqual(app.name, "nandy-io-people-api")
        self.assertEqual(str(app.mysql.engine.url), "mysql+pymysql://root@nandyio-people-api-mysql:3306/nandy_people")

        self.assertEqual(app.logger.name, "nandy-io-people-api")

        self.assertLogged(app.logger, "debug", "init", extra={
            "init": {
                "mysql": {
                    "connection": "mysql+pymysql://root@nandyio-people-api-mysql:3306/nandy_people"
                }
            }
        })


class TestHealth(TestRestful):

    def test_get(self):

        self.assertEqual(self.api.get("/health").json, {"message": "OK"})


class TestGroup(TestRestful):

    @unittest.mock.patch("requests.get")
    def test_get(self, mock_get):

        mock_get.return_value.json.return_value = [{
            "name": "unit",
            "url": "test"
        }]

        self.assertEqual(self.api.get("/group").json, {"group": [{
            "name": "unit",
            "url": "test"
        }]})

        mock_get.assert_has_calls([
            unittest.mock.call("http://api.klot-io/app/people.nandy.io/member"),
            unittest.mock.call().raise_for_status(),
            unittest.mock.call().json()
        ])


class TestPerson(TestRestful):

    def test_post(self):

        response = self.api.post("/person", json={
            "person": {
                "name": "unit",
                "data": {"a": 1}
            }
        })

        self.assertStatusModel(response, 201, "person", {
            "name": "unit",
            "data": {"a": 1}
        })

    def test_get(self):

        person = self.sample.person("unit")

        self.assertStatusModel(self.api.get(f"/person/{person.id}"), 200, "person", {
            "name": "unit"
        })


class TestIntegrate(TestRestful):

    def test_options(self):

        person = self.sample.person("unit")

        response = self.api.options("/integrate")

        self.assertEqual(response.json, {
            "options": [person.id],
            "labels": {str(person.id): 'unit'}
        })
        self.assertEqual(response.status_code, 200)

        self.assertLogged(self.app.logger, "debug", "response", extra={
            "response": {
                "status_code": 200,
                "json": {
                    "options": [person.id],
                    "labels": {person.id: 'unit'}
                }
            }
        })

    def test_get(self):

        person = self.sample.person("unit")

        self.assertStatusValue(self.api.get(f"/integrate"), 400, "message", "missing name")

        response = self.api.get(f"/integrate?name=unit")

        self.assertStatusModel(response, 200, "person", {
            "id": person.id,
            "name": "unit"
        })

        self.assertLogged(self.app.logger, "debug", "response", extra={
            "response": {
                "status_code": 200,
                "json": response.json
            }
        })
