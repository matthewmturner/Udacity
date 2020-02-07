# Udacity Full Stack Nanodegree: Project 1 - News Site Logs Analysis

## Introduction

This project is for the first project of Udacity's Full Stack Nanodegree program.  It is meant as a way to use skills that have been learned through the first 3 lessons of the program.  Thus far the content has been focused on networking/Linux basics and interacting with databases through SQL and Python.  The project is simulating the following scenario:

*You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.*

## Deliverables

The deliverables for the succesful completion of this project are the following:

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## Dependencies

To succesfully run this code one should have the following installed:

* [Python 3](https://www.python.org/downloads/) - The program scripts are written in Python 3. A few additional libraries are required to run the program and can be installed from the command line using `pip install` followed by the library name. The following are the required libraries:
  * psycopg2
  * pprint
  * csv
* [Virtualbox](https://www.virtualbox.org/) - This is the virtualization program for enabling a Linux VM on your machine.
* [Vagrant](https://www.vagrantup.com/downloads.html) - This is the wrapper that facilitates an easier setup of the VM on your machine.
* [PostgreSQL](https://www.postgresql.org/download/) - This is the database software used and should be installed on the VM.

The database and data required for this can be found [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).  The database is called 'news'.  This SQL file needs to be run after the VM and database software are installed.

A view was created on the logs data to simplify the matching of logs data with article data.  Specifically, the slug was extracted from the log path and only paths that lead to an article were kept.  The following is the SQL used to create this view.  This view is used for deliverable 1.

`create view v_article_slug_log as select substring(path from 10) as slug, ip, method, status, time, id from log where path like '/article/%';`

## Functions

A function was created for each deliverable.

### Deliverable 1: Top Articles

The function `top_articles(num_results=None, article_source='articles')` is used for extracting a sorted list of all the top articles (those with the most page visits).

#### Top Articles Parameters

* num_results = An integer used to specify how many top article results the user wants returned.

* article_source = Either the default value 'articles' or 'logs'.  Articles limits the list of shown articles to those in the articles table.  Choosing 'logs' takes any slug that was within the 'article' slug hierarchy and assumed that the article was the text after 'article/'.

### Deliverable 2: Top Authors

The function `top_authors(num_results=None)` is used for extracting a sorted list of the top authors (sum of page visits by author of articles).

#### Top Authors Parameters

* num_results = An integer used to specify how many top author results the user wants returned.

### Deliverable 3: Top Days with Errors

The function `top_error_days(days=None)` is used for getting a sorted list of days when there was the highest proportion of '404 NOT FOUND' errors when trying to access web pages.

#### Top Days with Errors Parameters

* days = An integer used to specificy how many days of error data the user wants returned.