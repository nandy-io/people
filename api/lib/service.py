"""
Module for the People API
"""

import flask
import flask_restful

import klotio
import klotio_flask_restful
import klotio_sqlalchemy_restful

import nandyio_people_models

def build():
    """
    Creates the Flask App
    """

    app = flask.Flask("nandy-io-people-api")

    app.mysql = nandyio_people_models.MySQL()

    api = flask_restful.Api(app)

    api.add_resource(klotio_flask_restful.Health, '/health')
    api.add_resource(Group, '/group')
    api.add_resource(PersonCL, '/person')
    api.add_resource(PersonRUD, '/person/<int:id>')
    api.add_resource(Integrate, '/integrate')

    app.logger = klotio.logger(app.name)

    app.logger.debug("init", extra={
        "init": {
            "mysql": {
                "connection": str(app.mysql.engine.url)
            }
        }
    })

    return app


class Group(klotio_flask_restful.Group):
    """
    Group class for People to get its members
    """

    APP = "people.nandy.io"


class Person(klotio_sqlalchemy_restful.Model):
    """
    Base Person class for attributes
    """

    SINGULAR = "person"
    PLURAL = "persons"
    MODEL = nandyio_people_models.Person
    ORDER = [nandyio_people_models.Person.name]

    FIELDS = [
        {
            "name": "name"
        }
    ]

class PersonCL(Person, klotio_sqlalchemy_restful.ModelCL):
    """
    Person Restful class for Creating and Listing
    """

class PersonRUD(Person, klotio_sqlalchemy_restful.ModelRUD):
    """
    Person Restful class for Retrievin, Updating, and Deleting
    """


class Integrate(Person, flask_restful.Resource):
    """
    Integration endpoints
    """

    @klotio_flask_restful.logger
    @klotio_sqlalchemy_restful.session
    def options(self):
        """
        OPTIONS endpoint to add fields for speech
        """

        choices = self.choices()

        return {"options": choices[0], "labels": choices[1]}

    @klotio_flask_restful.logger
    @klotio_sqlalchemy_restful.session
    def get(self):
        """
        GET endpoint to lookup people by name
        """

        if "name" not in flask.request.args:
            return {"message": "missing name"}, 400

        person = flask.request.session.query(
            nandyio_people_models.Person
        ).filter_by(
            name=flask.request.args['name']
        ).one()

        return {"person": self.response(person)}
