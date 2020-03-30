#!/usr/bin/python3
"""Module for DBstorage"""
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        print("CHEEEEEES", cls)
        dicty = {}
        try:
            if cls:
                if type(cls) is str:
                    cls = eval(cls)
                query = self.__session.query(cls)
                for obj in query:
                    key = "{}.{}".format(type(obj).__class__, obj.id)
                    dicty[key] = obj
            else:
                objects = [State, City, Place, User, Amenity, Review]
                for i in objects:
                    query = self.__session.query(i)
                    for obj in query:
                        key = "{}.{}".format(type(obj).__class__, obj.id)
                        dicty[key] = obj

            return dicty
        except:
            pass

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        try:
            self.__session.commit()
        except:
            pass

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        scp_session = scoped_session(Session)
        self.__session = scp_session()


    # self.__session.close()
