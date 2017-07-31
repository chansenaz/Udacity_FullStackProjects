# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Item, Category, CATEGORY_LIST

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

# Create dummy users
user_to_add = User(name="Fernando Hippokrates", email="fhippokrates@notreal.com",
                   picture='https://upload.wikimedia.org/wikipedia/commons/0/0d/Kangaroo_and_joey03.jpg')
session.add(user_to_add)
session.commit()

user_to_add = User(name="Rishi Trevelyan", email="rtrvelyan@notreal.com",
                   picture='https://s-media-cache-ak0.pinimg.com/736x/8a/b8/53/8ab853a3ce417f5c872e605abdaae6a9--panda-bears-god.jpg')
session.add(user_to_add)
session.commit()

user_to_add = User(name="Hubert Marcus", email="hmarcus@notreal.com",
                   picture='http://www.kidzone.ws/images-changed/penguins/adelie-penguin.jpg')
session.add(user_to_add)
session.commit()

user_to_add = User(name="Silvanus Vulcanus", email="svulcanus@notreal.com",
                   picture='https://upload.wikimedia.org/wikipedia/commons/a/ac/Cheetah_portrait_Whipsnade_Zoo.jpg')
session.add(user_to_add)
session.commit()

user_to_add = User(name="Staffan Raginhard", email="sraginhard@notreal.com",
                   picture='https://c402277.ssl.cf1.rackcdn.com/photos/6518/images/story_full_width/iStock_000011145477Large_mini_%281%29.jpg?1394632882')
session.add(user_to_add)
session.commit()

# Add categories
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

# Create bread/bakery items
item_to_add = Item(category_id=2, name='Sourdough Loaf', user_id=2,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Wheat Loaf', user_id=2,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='White Loaf', user_id=2,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='French Bread', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Artisan Baguette', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='San Francisco style', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Jalapeno Focaccia', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Italian Focaccia', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Hot Dog Buns', user_id=2,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Hamburger Buns', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Tortillas', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Dinner Rolls', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Hawaiian Rolls', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Bagels', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Cinnamon Rolls', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Chocolate Donut', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Apple Fritter', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Boston Creme', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Maple Bar', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Blueberry Muffin', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Banana Nut Muffin', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Lemon Poppyseed Muffin', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=2, name='Birthday Cake', user_id=3,
                   description="")
session.add(item_to_add)
session.commit()

# Create Canned/Jarred Goods items
item_to_add = Item(category_id=3, name='Green Beans', user_id=4,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=3, name='Spaghetti Sauce', user_id=4,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=3, name='Ketchup', user_id=5,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=3, name='Mustard', user_id=5,
                   description="")
session.add(item_to_add)
session.commit()

# Create dairy items
item_to_add = Item(category_id=4, name='Milk', user_id=5,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=4, name='Eggs', user_id=5,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=4, name='Cheese', user_id=5,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=4, name='Butter', user_id=5,
                   description="")
session.add(item_to_add)
session.commit()

item_to_add = Item(category_id=4, name='Yogurt', user_id=5,
                   description="")
session.add(item_to_add)
session.commit()

# Create dry/baked goods items

# Create frozen food items

# Create meat items

# Create produce items

# Create cleaner items

# Create paper goods items

# Create personal care items

# Leave 'other' items empty
