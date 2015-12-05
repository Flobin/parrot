#Parrot

This is a learning project that I’m doing for fun to teach myself how to build web apps. It is intended to be a kind of reddit clone. It will use Django, and probably some other stuff as well. I didn’t—well, still don’t know what to call it, so for now ‘Parrot’ will do.

## Prerequisites

You will need the following things properly installed on your computer.

* [Git](http://git-scm.com/)
* [Python](https://www.python.org/)
* [Node.js](http://nodejs.org/) (with NPM)

## Installation

* `git clone https://github.com/Flobin/parrot.git` this repository
* change into the new directory
* (optional) set up a virtual environment
* `pip install -r requirements.txt`
* `cd posts/static/posts`
* `npm install`

## Running / Development

* (optional) go into your virtualenv
* `python manage.py runserver`

And if you want to change templates/css:

* `cd posts/static/posts`
* `gulp watch`

Manage data in the admin panel:

* `python manage.py createsuperuser`
* go to `http://localhost:8000/admin` and log in

### Running Tests

* `python manage.py test posts`
* `python manage.py test functional_tests` (broken as of right now)

### Deploying

No idea yet

## To do list

* Upgrade to Django 1.9
* Restrict voting to 1 vote per user per link
* Enable sorting for comments and links
    * Sorting by time (current)
    * Sorting by score and time (like reddit)
    * Sorting by upvotes/downvotes
    * Only showing posts from a certain time period
* <del>Pagination for links</del>
* Pagination for comments (?)
* Restrict nesting for comments (maybe)
* Sign up / log in:
    * Style templates
    * Write proper test
* Switch to proper database (probably Postgres)
* Figure out deployment
* Add pages (about, etc.)
