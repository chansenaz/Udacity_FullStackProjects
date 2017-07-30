from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Item, Category

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
user_to_add = User(name="Fernando Hippokrates", email="fhippokrates@notreal.com",
             picture='https://upload.wikimedia.org/wikipedia/commons/0/0d/Kangaroo_and_joey03.jpg')
session.add(user_to_add)
session.commit()

# Create categories
CATEGORY_LIST = ['Beverages', 'Bread/Bakery', 'Canned/Jarred Goods', 'Dairy', 'Dry/Baking Goods', 'Frozen Foods',
                 'Meat', 'Produce', 'Cleaners', 'Paper Goods', 'Personal Care', 'Other']

cat_to_add = Category(name=CATEGORY_LIST[0])
session.add(cat_to_add)
session.commit()

cat_to_add = Category(name=CATEGORY_LIST[1])
session.add(cat_to_add)
session.commit()

cat_to_add = Category(name=CATEGORY_LIST[2])
session.add(cat_to_add)
session.commit()

cat_to_add = Category(name=CATEGORY_LIST[3])
session.add(cat_to_add)
session.commit()

cat_to_add = Category(name=CATEGORY_LIST[4])
session.add(cat_to_add)
session.commit()

cat_to_add = Category(name=CATEGORY_LIST[5])
session.add(cat_to_add)
session.commit()

cat_to_add = Category(name=CATEGORY_LIST[6])
session.add(cat_to_add)
session.commit()

cat_to_add = Category(name=CATEGORY_LIST[7])
session.add(cat_to_add)
session.commit()

cat_to_add = Category(name=CATEGORY_LIST[8])
session.add(cat_to_add)
session.commit()

cat_to_add = Category(name=CATEGORY_LIST[9])
session.add(cat_to_add)
session.commit()

cat_to_add = Category(name=CATEGORY_LIST[10])
session.add(cat_to_add)
session.commit()

cat_to_add = Category(name=CATEGORY_LIST[11])
session.add(cat_to_add)
session.commit()

# Create Beverage Items
item_to_add = Item(category_id=1, name='Cranberry Juice', user_id=1,
             description="100% juice made with the crisp, clean taste of real cranberries. No added sugar, " +
                         "a daily dose of vitamin C, and one cup of fruit, so it tastes good and " +
                         "it's good for you, too!")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=1, name='Coca Cola', user_id=1, description="Good ol' classic Coke!")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=1, name='Coffee', user_id=1,
             description="Occasional indulgence for some, a necessity for others.")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=1, name='Iced Tea', user_id=1,
                   description="Tasty and refreshing! Black tea made from real tea leaves.")
session.add(item_to_add)
session.commit()
