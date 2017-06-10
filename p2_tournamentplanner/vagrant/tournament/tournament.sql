-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- Useful psql commands:
-- '\i tournament.sql' to execute the tournament.sql file
-- '\l' to see a list of databases in psql mode
-- '\dt' to see a list of tables in a database

-- before running the CREATE TABLE statements do:

--1. 'createdb tournament'
--2. 'psql tournament'

--once you are in the tournament database, you can make tables:

CREATE TABLE matches  ( matchid serial primary key,
						player1 integer not null,
						player2 integer not null,
						winner integer not null
						);
						
						
CREATE TABLE players  ( playerid serial primary key,
						name varchar(100) not null );
						
						
INSERT INTO players (playerid, name) VALUES (DEFAULT, 'Lisa');
INSERT INTO players (playerid, name) VALUES (DEFAULT, 'Andrew');
INSERT INTO players (playerid, name) VALUES (DEFAULT, 'Simon');
						
						
--CREATE TABLE posts  ( content varchar (500) not null,
  --                      time timestamp default current_timestamp,
	--					id serial primary key);

						
						
						
						