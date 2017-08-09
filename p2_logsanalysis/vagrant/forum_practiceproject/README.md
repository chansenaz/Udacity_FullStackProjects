# Forum
Christopher Hansen - [github](https://github.com/chansenaz)

### About
This is a test/example project for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

### Features
Uses psycopg2 to keep a database of posts which are displayed as a forum thread. Uses bleach to sanitize user input.


### How to Use
Clone this repository to your local machine

In the 'vagrant' directory, using git/bash do 'vagrant up'

After vagrant has started up, do 'vagrant ssh'

Once connected, 'cd /vagrant/forum'
'python forum.py'
Open http://localhost:8000/ in your browser
You can now post messages and view the messages in the forum database!
