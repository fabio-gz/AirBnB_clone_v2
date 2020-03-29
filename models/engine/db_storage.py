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

        os.environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
        os.environ['HBNB_MYSQL_PWD'] = 'hbnb_dev_pwd'
        os.environ['HBNB_MYSQL_HOST'] = 'locahost'
        os.environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'
        os.environ['HBNB_ENV'] = 'dev'

        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        LH = os.getenv('HBNB_MYSQL_HOST')
        DB = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://user:pwd@LH:3306/DB',
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') is "test":
            
