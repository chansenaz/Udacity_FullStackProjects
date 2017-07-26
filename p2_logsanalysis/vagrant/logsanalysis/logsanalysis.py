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


def printQuery(title, results, print_type):
    print("\n" + title + "\n")
    for result in results:
        if print_type == 'view':
            print ('    ' + str(result[0]) + ' -- ' +
                   str(result[1]) + ' views')
        elif print_type == 'error':
            print ('    ' + str(result[0]) + ' -- ' +
                   str(result[1]) + '% errors')
    print("\n")


def main():
    # 1. What are the most popular three articles of all time?
    query1 = '''select title, num_views from viewcount_view limit 3;'''
    printQuery("1. What are the most popular three articles of all time?",
                   runQuery(query1, True), 'view')

    # 2. Who are the most popular article authors of all time?
    query2 = '''select authors.name, sum(num_views) as views_sum from
    viewcount_view, authors where authors.id = viewcount_view.author
    group by authors.name order by views_sum desc;'''
    printQuery("2. Who are the most popular article authors of all time?",
                   runQuery(query2, True), 'view')

    # 3. On which days did more than 1% of requests lead to errors?
    query3 = '''select * from errors_view where percent_error > 1'''
    printQuery("3. On which days did more than 1% of requests " +
                    "lead to errors?",
                    runQuery(query3, True), 'error')


if __name__ == '__main__':
    main()
