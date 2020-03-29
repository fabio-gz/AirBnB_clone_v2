#!/usr/bin/python3
"""Module for DBstorage"""
import os
from sqlalchemy import (create_engine)

class DBStorage:
    """Class for save in DB"""

    __engine = None
    __session = None


    def __init__(self):
        """The init return the instance"""

        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        LH = os.getenv('HBNB_MYSQL_HOST')
        DB = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(user, pwd, LH, DB),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') is "test":
            Base.metada.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the database session and output a dict"""
        
