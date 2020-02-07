#!/usr/bin/env python3

import psycopg2
from pprint import pprint
import csv

DBNAME = 'news'
try:
    db = psycopg2.connect(database=DBNAME)
except:
    print ("Unable to connect to the database")


def top_articles(num_results=None, article_source='articles', save=False):

    valid_sources = {'articles', 'logs'}
    if article_source not in valid_sources:
        raise ValueError("Invalid article source")

    c = db.cursor()

    if article_source == 'articles':

        c.execute("""
        SELECT articles.title, count(v_article_slug_log.slug) as views
        FROM articles LEFT JOIN v_article_slug_log
            ON articles.slug = v_article_slug_log.slug
        GROUP BY articles.slug, articles.title
        ORDER BY views DESC;
        """)

        col_names = [col[0] for col in c.description]
        raw_results = c.fetchall()
        top_results = raw_results[:num_results]

        results_list = []
        results_list.append(col_names)
        for r in top_results:
            row_list = []
            row_list.append(r[0])
            row_list.append(str(r[1]))
            results_list.append(row_list)

        if save is True:
            with open('top_articles.csv', 'w') as f:
                writer = csv.writer(f)
                writer.writerows(results_list)

        return results_list

    else:

        c.execute("""
        SELECT slug, count(*) as views
        FROM v_article_slug_log
        GROUP BY slug
        ORDER BY views DESC;
        """)

        col_names = [col[0] for col in c.description]
        raw_results = c.fetchall()
        top_results = raw_results[:num_results]

        results_list = []
        results_list.append(col_names)
        for r in top_results:
            row_list = []
            row_list.append(r[0])
            row_list.append(str(r[1]))
            results_list.append(row_list)

        if save is True:
            with open('top_articles.csv', 'w') as f:
                writer = csv.writer(f)
                writer.writerows(results_list)

        return results_list


def top_authors(num_results=None, save=False):

    c = db.cursor()

    c.execute("""
        SELECT name, count(v_article_slug_log.slug) as views
        FROM articles
            LEFT JOIN v_article_slug_log
                ON articles.slug = v_article_slug_log.slug
            LEFT JOIN authors ON articles.author = authors.id
        GROUP BY name
        ORDER BY views DESC;
        """)

    col_names = [col[0] for col in c.description]
    raw_results = c.fetchall()
    top_results = raw_results[:num_results]

    results_list = []
    results_list.append(col_names)
    for r in top_results:
        row_list = []
        row_list.append(r[0])
        row_list.append(str(r[1]))
        results_list.append(row_list)

    if save is True:
        with open('top_authors.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(results_list)

    return results_list


def top_error_days(days=None, save=False):

    c = db.cursor()

    c.execute("""
        SELECT to_char(date_trunc('day', time), 'YYYY-Mon-DD') AS day,
        count(CASE WHEN status IN ('200 OK') THEN 1 ELSE NULL END)
            AS status_okay,
        count(CASE WHEN status IN ('404 NOT FOUND') THEN 1 ELSE NULL END)
            AS status_bad,
        count(*) AS status_total,
        round(count(CASE WHEN status IN ('404 NOT FOUND') THEN 1
            ELSE NULL END)::numeric * 100 / count(*)::numeric, 2)
            AS status_percent_bad
        FROM log
        GROUP BY 1
        ORDER BY status_percent_bad DESC;
        """)

    col_names = [col[0] for col in c.description]
    raw_results = c.fetchall()
    top_results = raw_results[:days]

    results_list = []
    results_list.append(col_names)
    for r in top_results:
        row_list = []
        row_list.append(r[0])
        row_list.append(str(r[1]))
        row_list.append(str(r[2]))
        row_list.append(str(r[3]))
        row_list.append(str(r[4]))
        results_list.append(row_list)

    if save is True:
        with open('top_error_days.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(results_list)

    return results_list


if __name__ == '__main__':
    pprint(top_articles(num_results=5, article_source='articles'))
    pprint(top_authors())
    pprint(top_error_days(days=5))
