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


drop table players CASCADE;
drop table matches;


CREATE TABLE players  ( playerid serial primary key,
						name varchar(100) not null );
						
						
						
CREATE TABLE matches  ( matchid serial primary key,
						winner integer references players(playerid),
						loser integer references players(playerid)
						);
					



		

	
						
						