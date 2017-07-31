# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, \
    redirect, url_for, flash, jsonify
from sqlalchemy import create_engine, desc, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Item, Category, CATEGORY_LIST
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Item Catalog Application"

# Connect to Database and create database session
engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create anti-forgery state token
@app.route('/login')
def show_login():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


# Connect to facebook account and create a new user (if new email)
@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print "access token received %s " % access_token

    app_id = json.loads(open('fb_client_secrets.json', 'r').read())[
        'web']['app_id']
    app_secret = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exc' \
          'hange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (
              app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]

    # Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.8/me"

    # Due to the formatting for the result from the server token exchange
    # we have to split the token first on commas and select the first
    # index which gives us the key : value for the server access token then
    # we split it on colons to pull out the actual token value and replace
    # the remaining quotes with nothing so that it can be used directly in
    # the graph api calls
    token = result.split(',')[0].split(':')[1].replace('"', '')

    url = 'https://graph.facebook.com/v2.8/me?access_token=%s&fields=name' \
          ',id,email' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    # print "url sent for API access:%s"% url
    # print "API JSON result: %s" % result
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

    # The token is stored in the login_session in order to properly logout
    login_session['access_token'] = token

    # Get user picture
    url = 'https://graph.facebook.com/v2.8/me/picture?access_token=%s&redi' \
          'rect=0&height=200&width=200' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]

    # see if user exists
    user_id = get_userid(login_session['email'])
    if not user_id:
        user_id = create_user(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']

    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150' \
              'px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '

    flash("Now logged in as %s" % login_session['username'])
    return output


# log out of facebook account
@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % \
          (facebook_id, access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    return "you have been logged out"


# log in to google account
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already '
                                            'connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user's email exists, if it doesn't make a new user
    user_id = get_userid(data["email"])
    if not user_id:
        user_id = create_user(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px' \
              ';-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("You are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# User Helper Functions
# insert new user into database and return user id
def create_user(login_session):
    new_user = User(name=login_session['username'],
                    email=login_session['email'],
                    picture=login_session['picture'])
    session.add(new_user)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def get_userinfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


# if a google account and a facebook account have the same email,
# they are the same person
def get_userid(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# disconnect from google account and reset session
@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = credentials.access_token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] != '200':
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


# figure out how user is logged in and call appropriate disconnect function
# then delete login_session
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            # del login_session['credentials']
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
    else:
        flash("You were not logged in")

    return redirect(url_for('show_recent_items'))


# Show items from a single category
@app.route('/category/<int:category_id>')
def show_category(category_id):
    categories = session.query(Category).order_by(asc(Category.id)).all()
    items = session.query(Item).filter_by(category_id=category_id).all()
    category_name = session.query(Category).filter_by(id=category_id)[0]
    return render_template('category.html', items=items,
                           categories=categories, category_name=category_name)


# Show information for a single item
@app.route('/item/<int:item_id>')
def show_item(item_id):
    item_toshow = session.query(Item).filter_by(id=item_id)[0]
    permission = False
    if 'username' in login_session \
            and login_session['user_id'] == item_toshow.user_id:
        permission = True
    return render_template('item.html', item=item_toshow,
                           permission=permission,
                           category=CATEGORY_LIST[item_toshow.category_id - 1])


# Create a new item
@app.route('/item/new/', methods=['GET', 'POST'])
def new_item():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        user_item = Item(category_id=CATEGORY_LIST.index(
            request.form['category']) + 1, name=request.form['name'],
                         user_id=login_session['user_id'],
                         description=request.form['description'])
        session.add(user_item)
        flash('New Item %s Successfully Created' % user_item.name)
        session.commit()
        return redirect(url_for('show_recent_items'))
    else:
        return render_template('newitem.html', categories=CATEGORY_LIST)


# Edit an item
@app.route('/item/<int:item_id>/edit/', methods=['GET', 'POST'])
def edit_item(item_id):
    edited_item = session.query(Item).filter_by(id=item_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if edited_item.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not " \
               "authorized to edit this item. " \
               "You may only edit items that you have " \
               "created.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            edited_item.name = request.form['name']
        if request.form['category']:
            edited_item.category_id = \
                CATEGORY_LIST.index(request.form['category']) + 1
        if request.form['description']:
            edited_item.description = request.form['description']
        session.add(edited_item)
        session.commit()
        flash('Item %s Successfully Edited' % edited_item.name)
        return redirect(url_for('show_recent_items'))
    else:
        return render_template('edititem.html', item=edited_item,
                               categories=CATEGORY_LIST)


# Delete an item
@app.route('/item/<int:item_id>/delete/', methods=['GET', 'POST'])
def delete_item(item_id):
    if 'username' not in login_session:
        return redirect('/login')
    item_to_delete = session.query(Item).filter_by(id=item_id).one()
    if login_session['user_id'] != item_to_delete.user_id:
        return "<script>function myFunction() {alert('You are not authorized" \
               " to delete menu items to this restaurant. Please create your" \
               " own restaurant in order to delete items.');}</script><body " \
               "onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(item_to_delete)
        session.commit()
        flash('Item Successfully Deleted')
        return redirect(url_for('show_recent_items'))
    else:
        return render_template('deleteitem.html', item=item_to_delete)


# JSON API to view information for one Item
@app.route('/item/<int:item_id>/JSON')
def item_info_JSON(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    return jsonify(Item=item.serialize)


# JSON API to view information for all items
@app.route('/items/JSON')
def all_items_info_JSON():
    items = session.query(Item).all()
    return jsonify(Items=[i.serialize for i in items])


# JSON API to view information for all items of one category
@app.route('/category/<int:category_id>/JSON')
def category_items_info_JSON(category_id):
    items = session.query(Item).filter_by(category_id=category_id).all()
    return jsonify(Items=[i.serialize for i in items])


# Show most recently added items on the home page
@app.route('/')
@app.route('/home/')
def show_recent_items():
    categories = session.query(Category).order_by(asc(Category.id)).all()
    items = session.query(Item).order_by(desc(Item.id)).limit(19).all()
    return render_template('home.html', items=items, categories=categories)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
