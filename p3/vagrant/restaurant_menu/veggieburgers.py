from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


veggieBurgers = session.query(MenuItem).filter_by(name = "Veggie Burger")

for veggieBurger in veggieBurgers:
    print(veggieBurger.id)
    print(veggieBurger.price)
    print(veggieBurger.restaurant.name + "\n")
    
    
    
#select veggie burger with id = 10.
UrbanVeggieBurger = session.query(MenuItem).filter_by(id = 10).one()

#price is $5.99
print(UrbanVeggieBurger.price)

#Let's drop the price to $2.99
UrbanVeggieBurger.price = "$2.99"
session.add(UrbanVeggieBurger)
session.commit()




#now all the restaurants drop their burgers to $2.99
for veggieBurger in veggieBurgers:
    if veggieBurger.price != '$2.99':
        veggieBurger.price = '$2.99'
        session.add(veggieBurger)
        session.commit()
        
        
        
for veggieBurger in veggieBurgers:
    print(veggieBurger.id)
    print(veggieBurger.price)
    print(veggieBurger.restaurant.name + "\n")
    
    
    
#Now let's delete an item. Auntie Ann decides spinach ice cream was a bad idea
spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
print(spinach.restaurant.name)
session.delete(spinach)
session.commit()
spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()


