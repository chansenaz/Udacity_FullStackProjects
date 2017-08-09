# News Website Logs Analysis
Christopher Hansen - [github](https://github.com/chansenaz)

### About
This is my second project for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

### Features
Uses vagrant to query a PostgreSQL database of articles, authors, and log entries. The structure of the database can be seen in vagrant/logsanalysis/database_description.txt.

This program answers three questions about the news website's traffic:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?


### How to Use

##### Requirements
1. Python (2 or 3)
2. Vagrant
3. VirtualBox

##### Setup
1. Clone this repository to your local machine
2. Unzip newsdata.sql from newsdata.zip
3. In the 'vagrant' directory, using git/bash do 'vagrant up'
4. After vagrant has started up, do 'vagrant ssh'
5. Once connected, 'cd /vagrant/logsanalysis'
6. 'psql -d news -f newsdata.sql' to import the data into database 'news'
7. 'psql news' to go into psql mode in the news database.
8. Make view for querying viewcounts:
	create view viewcount_view as
    select title, author, count(*) as num_views from articles, log
    where log.path = concat('/article/', articles.slug)
	group by articles.title, articles.author order by num_views desc;
9. Make view for querying errors:
	create view errors_view as select date(time),
	round(100.0 * sum(case log.status when '200 OK' then 0 else 1 end) /
	count(log.status), 1) as percent_error from log group by date(time)
	order by percent_error desc;
10. 'python logsanalysis.py' to run the program
