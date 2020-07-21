import flask
import flask_restful

import mysql
import klotio.service

def app():

    app = flask.Flask("nandy-io-speech-api")

    app.mysql = mysql.MySQL()

    api = flask_restful.Api(app)

    api.add_resource(klotio.service.Health, '/health')
    api.add_resource(Group, '/group')
    api.add_resource(PersonCL, '/person')
    api.add_resource(PersonRUD, '/person/<int:id>')

    return app


class Group(klotio.service.Group):
    APP = "people.nandy.io"


class Person(klotio.service.Model):

    SINGULAR = "person"
    PLURAL = "persons"
    MODEL = mysql.Person
    ORDER = [mysql.Person.name]

    FIELDS = [
        {
            "name": "name"
        }
    ]

class PersonCL(Person, klotio.service.RestCL):
    pass

class PersonRUD(Person, klotio.service.RestRUD):
    pass
