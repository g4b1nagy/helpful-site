Helpful Site
============

Beautifully simple static site generator in Python

### What's this? ###

Helpful Site is a static site generator written on top of
[Python-Markdown](http://pythonhosted.org/Markdown/),
[Jinja2](http://jinja.pocoo.org/) and
[Crammit](https://github.com/rspivak/crammit). It aims to provide a friendly
interface for building web pages from markdown and minifying css and js files.
You can check out a rendering of the sample pages here =>
http://helpfulsheep.com/hs/

Specifically, Helpful Site provides you with:

* post categories
* home and category pages that provide lists of posts
* pagination for the posts on the home page
* previous post and next post links
* ability to mark out the excerpt using the `<!--more-->` keyword
* support for per page attributes such as description, ogimage, style
and script
* syntax highlighting of code blocks
* the great looking Casper theme from [Ghost](https://ghost.org/)
* friendly config.yaml file
* flexible template system
* static web server to try your site out locally

### How does it work? ###

The project provides a number of `./manage.py` commands that use the files
from the src directory to generate a static site inside the dist directory.

To create a new page, run

    ./manage.py new

After adding content to the page, dun

    ./manage.py build

to build the html files. If you plan to serve your site from a subdirectory
such as http://www.example.com/blog/, you should update the config.yaml file
and run

    ./manage.py build --prod

To update the css and js files, you should run

    ./manage.py mini

You can also run

    ./manage.py reset

to remove the entire dist folder and

    ./manage.py reset --all

to remove the src folder as well. You can run

    ./manage.py runserver

to start a local server and last but not least,

    ./manage.py update

to both minify and build the files.

### Getting your hands dirty ###

* cd to a comfy location
* git clone git@github.com:g4b1nagy/helpful-site.git
* cd helpful-site/
* virtualenv .venv
* source .venv/bin/activate
* pip install -r config/requirements.txt
* ./manage.py update
* ./manage.py runserver
* point your browser to [http://localhost:3000/](http://localhost:3000/)

Building your site on top of this should be a matter of customizing the files
in the config directory i.e. config.yaml and template files and adding your
own css and js files to the src directory. As far as media goes, there is
no recommended strategy, but you could store your files inside each post's
directory and use relative links to point to them. This should provide the
greatest flexibility while also keeping your posts atomic - limited to a
single directory.

### Known issues ###

Google Chrome seems to screw up the font size from time to time when loading
the pages. According to [this post](http://stackoverflow.com/questions/20845183/inconsistent-font-size-rendering-issue-on-chrome),
it seems to be caused by using rem units in the css files.

If you do funky stuff, such as delete the dist folder while the server is
running, you might end up with a `socket.error: [Errno 98] Address already in use`
error when trying to restart it. You will need to manually find the server
process and `kill -9` it.

Yes, this is written in Python 2. I am sorry. No, there are no tests.
I am even sorrier for that.

### Feeling generous? ###

Contributions are more than welcome and are generally rewarded with a huge
THANK YOU! and a [virtual] hug. Feel free to tackle any issues you may have
and send me a pull request afterwards.

If you have bigger plans, feel free to drop me a line at gabi@helpfulsheep.com.