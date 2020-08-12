import sqlalchemy
import sqlalchemy.ext.mutable
import sqlalchemy_jsonfield

import klotio_sqlalchemy_models


class MySQL(klotio_sqlalchemy_models.MySQL):

    DATABASE = "nandy_people"


class Person(MySQL.Base):

    __tablename__ = "person"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(64), nullable=False)
    data = sqlalchemy.Column(
        sqlalchemy.ext.mutable.MutableDict.as_mutable(
            sqlalchemy_jsonfield.JSONField(enforce_string=True,enforce_unicode=False)
        ),
        nullable=False,
        default=dict
    )

    sqlalchemy.schema.UniqueConstraint('name', name='label')

    def __repr__(self):
        return "<Person(name='%s')>" % (self.name)
