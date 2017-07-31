# Grocery Store Item Catalog
Christopher Hansen - [github](https://github.com/chansenaz)

### About
This is my third project for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

### Features
This application allows a user to monitor the items in stock at a grocery store. The homepage displays the most recently added items and a list of all the categories. If a user clicks on a category, they can view all of the items in the catalog under that category. Clicking on a specific item will allow a user to see its full description.

Users are also able to login to the page using their google account or their facebook account. A logged in user can add their own items to the catalog. Users can also modify or delete items that they have created.

Users are recognized by their email address, so if you have a facebook account and a google account with the same email, either login will allow you to modify/delete your own items.

Finally, JSON endpoints are available for viewing specific items, all of the items, and all of the items under a specific category.

### Requirements
* Python 2.7
* Flask, sqlalchemy, oauth2client


### How to Use

1. Clone a copy of this repository and cd to p3_itemcatalog/itemcatalog

		git@github.com:chansenaz/Udacity_FullStackProjects.git
		
2. Run database_setup.py to establish the database

		python database_setup.py

3. Run populate_items.py to fill the database

		python populate_items.py

4. Run item_catalog.py to start the webserver. ctrl+c when you are done

		python item_catalog.py

5. Open a web browser and open URL:

		localhost:8000
		
6. To view JSON Endpoints use the following URLs:

* All items:

		localhost:8000/items/JSON
        
* One item:

		localhost:8000/item/<item_id#>/JSON

* All items from one category:

		localhost:8000/category/<category_id#>/JSON