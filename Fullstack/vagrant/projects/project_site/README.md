# Udacity Full Stack Nanodegree: Project 2 - Project Organizer (Item Catalog)

## Introduction

This project is the second project of Udacity's Full Stack Nanodegree program.  It is meant as a way to use web development skills that have been learned such as Flask, Authentication/Authorization, and APIs, among the previously learned database and networking skills.   This Project Organizer is meant to act as a task repository for all projects that a person is working on.

## Requirements

The requirements for the succesful completion of this project are the following:

1. JSON endpoint for stored data

2. All CRUD operations

3. Authentication and authorization status must be taken into account when submitting CRUD operations.

4. Third party authentication and authorization service must be used.

5. Login and logout buttons must be present.

## Dependencies

To succesfully run this code one should have the following installed:

* [Python 2](https://www.python.org/downloads/) - The program scripts are written in Python 3. A few additional libraries are required to run the program and can be installed from the command line using `pip install` followed by the library name. The following are the required libraries:
  * Flask
  * sqlalchemy
  * httplib2
  * random
  * string
  * json
  * datetime
* [Virtualbox](https://www.virtualbox.org/) - This is the virtualization program for enabling a Linux VM on your machine.
* [Vagrant](https://www.vagrantup.com/downloads.html) - This is the wrapper that facilitates an easier setup of the VM on your machine.
* [SQLite](https://sqlite.org/download.html) - This is the database software used and should be installed on the VM.


### Step 1: Clone Repository

All required project files can be found in the following GitHub Repository.
Link: https://github.com/mturner737/udacity-fullstack/tree/master/vagrant/projects/project_site

### Step 2: Install VM

The VM setup can be found in the VagrantFile in this GitHub location.
https://github.com/mturner737/udacity-fullstack/tree/master/vagrant

### Step 3: Run Web Server

On the VM run project_site.py to get the web server up and running.

### Step 4: Visit Website

Go to https://localhost:5000/projects/ in your browser to start using the site.

