#!/usr/bin/env python

import nandyio_people_models

nandyio_people_models.MySQL.create_database()
nandyio_people_models.MySQL.Base.metadata.create_all(nandyio_people_models.MySQL().engine)
