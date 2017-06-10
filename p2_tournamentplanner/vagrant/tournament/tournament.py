#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    
    return psycopg2.connect("dbname=tournament")


def runQuery(query, return_results):
    """Connect to the database, execute a query, return the query result (if appopriate),
    and close the database connection"""
    
    db = connect()
    c = db.cursor()
    c.execute(query)
    db.commit()
    
    if return_results:
        result = c.fetchall()
        db.close()
        return result
    else:
        db.close()
    
    

def deleteMatches():
    """Remove all the match records from the database."""
    
    query = "DELETE FROM matches;"
    runQuery(query, False)


def deletePlayers():
    """Remove all the player records from the database."""
    
    query = "DELETE FROM players;"
    runQuery(query, False)


def countPlayers():
    """Returns the number of players currently registered."""
    
    query = "SELECT COUNT(*) FROM players;"
    result = runQuery(query, True)
    
    numPlayers = int(result[0][0])
    return numPlayers


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO players (playerid, name) VALUES (DEFAULT, %s);", (bleach.clean(name),))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


