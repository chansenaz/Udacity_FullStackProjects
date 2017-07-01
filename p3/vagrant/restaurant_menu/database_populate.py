from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


#lets our program know which database engine we want to communicate with
engine = create_engine('sqlite:///restaurantmenu.db')

#Then, let's bind the engine to our Base class with the following command.
#This command just makes the connections between our class definitions and 
#the corresponding tables within our database.
Base.metadata.bind = engine


#Now create a session-maker object. This establishes a link of communication
#between our code execution and the engine we just created.
DBSession = sessionmaker(bind = engine)

#In order to create, read, or update information on our database, SQLAlchemy
#executes data operations via an interface called a session. A session allows
#us to write down all the commands we want to execute, but not send them to
#the database until we call a commit.
session = DBSession()

#From now on, when I want to make a change to the database, I can do it just by
#calling a method from within session. The DBSession object gives me a staging
#zone for all of the objects loaded into the database session object. Any change
#made to the objects in the session won't be persisted into the database until
#I call session.commit().

myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()


#check to make sure our change worked:
print(session.query(Restaurant).all())


cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)
session.add(cheesepizza)
session.commit()

print(session.query(MenuItem).all())