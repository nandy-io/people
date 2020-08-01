import flask
import flask_restful

import model
import klotio.api

def app():

    app = flask.Flask("nandy-io-speech-api")

    app.mysql = model.MySQL()

    api = flask_restful.Api(app)

    api.add_resource(klotio.api.Health, '/health')
    api.add_resource(Group, '/group')
    api.add_resource(PersonCL, '/person')
    api.add_resource(PersonRUD, '/person/<int:id>')
    api.add_resource(Integrate, '/integrate')

    return app


class Group(klotio.api.Group):
    APP = "people.nandy.io"


class Person(klotio.api.Model):

    SINGULAR = "person"
    PLURAL = "persons"
    MODEL = model.Person
    ORDER = [model.Person.name]

    FIELDS = [
        {
            "name": "name"
        }
    ]

class PersonCL(Person, klotio.api.RestCL):
    pass

class PersonRUD(Person, klotio.api.RestRUD):
    pass

class Integrate(PersonRUD):

    @klotio.api.require_session
    def options(self):

        choices = Person.choices()

        return {"options": choices[0], "labels": choices[1]}

    @klotio.api.require_session
    def get(self):

        if "name" not in flask.request.args:
            return {"message": "missing name"}, 400

        person = flask.request.session.query(
            model.Person
        ).filter_by(
            name=flask.request.args['name']
        ).one()

        return {"person": self.response(person)}