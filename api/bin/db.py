#!/usr/bin/env python

import klotio
import nandyio_people_models

logger = klotio.logger('nandy-io-people-db')

logger.debug("init", extra={
    "init": {
        "mysql": {
            "database": nandyio_people_models.MySQL.DATABASE
        }
    }
})

nandyio_people_models.MySQL.create_database()
nandyio_people_models.MySQL.Base.metadata.create_all(nandyio_people_models.MySQL().engine)
