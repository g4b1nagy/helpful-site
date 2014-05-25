helpful-site
============

Clever static site generator written in Python [work in progress]

### What's this? ###

helpful-site is a static site generator written on top of
[click](http://click.pocoo.org/), [Jinja2](http://jinja.pocoo.org/) and
[Crammit](https://github.com/rspivak/crammit). It aims to provide a friendly
interface for building web pages from markdown files and minifying CSS and JS.
Customizable template system and static web server included.

### How does it work? ###

The project provides a number of ./manage.py commands that use the files from
the src directory to generate a static site inside the dist directory.

To create a new page, run

    ./manage.py new

After adding content to the page, run

    ./manage.py compile

to build the .html files. If you make any changes to the CSS or JS inside the
src directory, you will want to run

    ./manage.py mini

to update the minified CSS and JS.

Run

    ./manage.py runserver

to start a local server and last but not least,

    ./manage.py update


to both minify and compile the files.

### Getting your hands dirty ###

* cd to a comfy location
* git clone git@github.com:g4b1nagy/helpful-site.git
* cd helpful-site/
* virtualenv .venv
* source .venv/bin/activate
* pip install -r config/requirements.txt
* customize the files in the config directory i.e. templates and yaml files
* add your own CSS and JS files to the src directory
* ./manage.py new
* add content to the page
* ./manage.py update
* ./manage.py runserver
* point your browser at [http://localhost:3000/](http://localhost:3000/)