import unittest
import unittest.mock
import klotio.unittest

import os
import json
import yaml

import flask
import opengui
import sqlalchemy.exc

import mysql
import test_mysql

import service


class TestRest(klotio.unittest.TestCase):

    maxDiff = None

    @classmethod
    def setUpClass(cls):

        cls.app = service.app()
        cls.api = cls.app.test_client()

    def setUp(self):

        self.app.mysql.drop_database()
        self.app.mysql.create_database()

        self.session = self.app.mysql.session()
        self.sample = test_mysql.Sample(self.session)

        self.app.mysql.Base.metadata.create_all(self.app.mysql.engine)

    def tearDown(self):

        self.session.close()
        self.app.mysql.drop_database()


class TestHealth(TestRest):

    def test_get(self):

        self.assertEqual(self.api.get("/health").json, {"message": "OK"})


class TestGroup(TestRest):

    @unittest.mock.patch.dict(os.environ, {
        "NODE_NAME": "barry"
    })
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
            unittest.mock.call("http://barry:8083/app/people.nandy.io/member"),
            unittest.mock.call().raise_for_status(),
            unittest.mock.call().json()
        ])


class TestPerson(TestRest):

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

        person_id = response.json["person"]["id"]

    def test_get(self):

        person = self.sample.person("unit")

        self.assertStatusModel(self.api.get(f"/person/{person.id}"), 200, "person", {
            "name": "unit"
        })
