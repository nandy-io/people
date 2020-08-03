import unittest
import unittest.mock

import models


class Sample:

    def __init__(self, session):

        self.session = session

    def person(self, name, data=None):

        people = self.session.query(models.Person).filter_by(name=name).all()

        if people:
            return people[0]

        person = models.Person(name=name, data=data)
        self.session.add(person)
        self.session.commit()

        return person

class TestMySQL(unittest.TestCase):

    maxDiff = None

    def setUp(self):

        self.mysql = models.MySQL()
        self.session = self.mysql.session()
        self.mysql.drop_database()
        self.mysql.create_database()
        self.mysql.Base.metadata.create_all(self.mysql.engine)

    def tearDown(self):

        self.session.close()
        self.mysql.drop_database()

    def test_Person(self):

        self.session.add(models.Person(
            name="unit",
            data={"a": 1}
        ))
        self.session.commit()

        person = self.session.query(models.Person).one()
        self.assertEqual(str(person), "<Person(name='unit')>")
        self.assertEqual(person.name, "unit")
        self.assertEqual(person.data, {"a": 1})

        person.data["a"] = 2
        self.session.commit()
        person = self.session.query(models.Person).one()
        self.assertEqual(person.data, {"a": 2})
