#!/usr/bin/env python2.7
# logsanalysis.py - implementation of a news website log analyzer
import psycopg2


def runQuery(query, return_results):
    # Connect to the database and execute the given query
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    db.commit()

    # If we are returning results, store the results
    # for return before closing connection
    if return_results:
        result = c.fetchall()
        db.close()
        return result
    else:
        db.close()


def printViewQuery(title, results):
    print("\n" + title + "\n")
    for result in results:
        print ('    ' + str(result[0]) + ' -- ' +
               str(result[1]) + ' views')
    print("\n")


def printErrorQuery(title, results):
    print("\n" + title + "\n")
    for result in results:
        print ('    ' + str(result[0]) + ' -- ' +
               str(result[1]) + '% errors')
    print("\n")


def main():
    # Create views for our queries. viewquery1 is for questions 1 and 2
    viewquery1 = '''create view viewcount_view as
    select title, author, count(*) as num_views from articles, log
    where log.path like concat('%',articles.slug) group by articles.title,
    articles.author order by num_views desc;'''
    try:
        runQuery(viewquery1, False)
    except:
        pass

    # viewquery2 is for question 3
    viewquery2 = '''create view errors_view as select date(time),
    round(100.0 * sum(case log.status when '200 OK' then 0 else 1 end) /
    count(log.status), 1) as percent_error from log group by date(time)
    order by percent_error desc;'''
    try:
        runQuery(viewquery2, False)
    except:
        pass

    # 1. What are the most popular three articles of all time?
    query1 = '''select title, num_views from viewcount_view limit 3;'''
    printViewQuery("1. What are the most popular three articles of all time?",
                   runQuery(query1, True))

    # 2. Who are the most popular article authors of all time?
    query2 = '''select authors.name, sum(num_views) as views_sum from
    viewcount_view, authors where authors.id = viewcount_view.author
    group by authors.name order by views_sum desc;'''
    printViewQuery("2. Who are the most popular article authors of all time?",
                   runQuery(query2, True))

    # 3. On which days did more than 1% of requests lead to errors?
    query3 = '''select * from errors_view where percent_error > 1'''
    printErrorQuery("3. On which days did more than 1% of requests " +
                    "lead to errors?",
                    runQuery(query3, True))


if __name__ == '__main__':
    main()
