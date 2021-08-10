'''DBStorage engine'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    '''Database storage engine'''
    __engine = None
    __session = None
    classes = [
        User,
        City,
        Place,
        State,
        Amenity,
        Review
    ]

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''Return all objects from database depending on class name'''
        all_dict = {}
        object_list = []
        if cls:
            object_list = self.__session.query(cls).all()
        else:
            for cs in classes:
                object_list += self.__session.query(cs)
        for obj in object_list:
            key = "{}.{}".format(obj.__class__.__name__, str(obj.id))
            all_dict[key] = obj
        return all_dict

    def new(self, obj):
        '''Add object to database session'''
        self.__session.add(obj)

    def save(self):
        '''Commit changes to the current session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''Delete from session'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''Create tables in the database'''
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    def close(self):
        '''Close the session'''
        self.__session.close()
