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
    api.add_resource(Integrate, '/integrate')

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

class Integrate(PersonRUD):

    @klotio.service.require_session
    def options(self):

        choices = Person.choices()

        return {"options": choices[0], "labels": choices[1]}

    @klotio.service.require_session
    def get(self):

        if "name" not in flask.request.args:
            return {"message": "missing name"}, 400

        person = flask.request.session.query(
            mysql.Person
        ).filter_by(
            name=flask.request.args['name']
        ).one()

        return {"person": self.response(person)}