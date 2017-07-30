from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Item, CATEGORY_LIST

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Fernando Hippokrates", email="fhippokrates@notreal.com",
             picture='https://upload.wikimedia.org/wikipedia/commons/0/0d/Kangaroo_and_joey03.jpg')
session.add(User1)
session.commit()

# Create Beverage Items
Item1 = Item(category=CATEGORY_LIST[0], name='Cranberry Juice', user_id=1)
session.add(Item1)
session.commit()

Item2 = Item(category=CATEGORY_LIST[0], name='Coca Cola', user_id=1)
session.add(Item2)
session.commit()

Item3 = Item(category=CATEGORY_LIST[0], name='Lemonade', user_id=1)
session.add(Item3)
session.commit()

Item4 = Item(category=CATEGORY_LIST[0], name='Iced Tea', user_id=1)
session.add(Item4)
session.commit()
