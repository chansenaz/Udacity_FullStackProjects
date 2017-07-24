# Forum
Christopher Hansen - [github](https://github.com/chansenaz)

### About
This is a test/example project for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

### Features
Uses vagrant to maintain a PostgreSQL database of players and matches. Every player has an id and a name and every match has an id, a winner, and a loser. The user can add players and matches, clear the players or matches tables, get the player standings, and generate a set of swiss pairs for the next round of the tournament.


### How to Use
Clone this repository to your local machine

In the 'vagrant' directory, using git/bash do 'vagrant up'

After vagrant has started up, do 'vagrant ssh'

Once connected, 'cd /vagrant/forum'
'python forum.py'
Open http://localhost:8000/ in your browser
You can now post messages and view the messages in the forum database!
