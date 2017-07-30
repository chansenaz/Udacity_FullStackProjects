from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

CATEGORY_LIST = ['Beverages', 'Bread/Bakery', 'Canned/Jarred Goods', 'Dairy', 'Dry/Baking Goods', 'Frozen Foods',
                 'Meat', 'Produce', 'Cleaners', 'Paper Goods', 'Personal Care', 'Other']


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    category = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category
        }


engine = create_engine('sqlite:///itemcatalog.db')

Base.metadata.create_all(engine)

