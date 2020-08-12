import flask
import flask_restful

import models
import klotio
import klotio_flask_restful
import klotio_sqlalchemy_restful

def app():

    app = flask.Flask("nandy-io-people-api")

    app.mysql = models.MySQL()

    api = flask_restful.Api(app)

    api.add_resource(klotio_flask_restful.Health, '/health')
    api.add_resource(Group, '/group')
    api.add_resource(PersonCL, '/person')
    api.add_resource(PersonRUD, '/person/<int:id>')
    api.add_resource(Integrate, '/integrate')

    app.logger = klotio.logger(app.name)

    app.logger.debug("settings", extra={
        "settings": {
            "mysql": str(app.mysql.engine.url)
        }
    })

    return app


class Group(klotio_flask_restful.Group):
    APP = "people.nandy.io"


class Person(klotio_sqlalchemy_restful.Model):

    SINGULAR = "person"
    PLURAL = "persons"
    MODEL = models.Person
    ORDER = [models.Person.name]

    FIELDS = [
        {
            "name": "name"
        }
    ]

class PersonCL(Person, klotio_sqlalchemy_restful.RestCL):
    pass

class PersonRUD(Person, klotio_sqlalchemy_restful.RestRUD):
    pass

class Integrate(PersonRUD):

    @klotio_flask_restful.logger
    @klotio_sqlalchemy_restful.session
    def options(self):

        choices = Person.choices()

        return {"options": choices[0], "labels": choices[1]}

    @klotio_flask_restful.logger
    @klotio_sqlalchemy_restful.session
    def get(self):

        if "name" not in flask.request.args:
            return {"message": "missing name"}, 400

        person = flask.request.session.query(
            models.Person
        ).filter_by(
            name=flask.request.args['name']
        ).one()

        return {"person": self.response(person)}
