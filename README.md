# url-share
A simple web app to share URLs across a network

Scenario:

You're on twitter and want to save a link to read it later.
There are a zillion ways to share stuff online, except none is pervasive and all require "cloud" storage. And let's be honest, the only thing everyone has is e-mail. So you have this link, but you don't want to e-mail it to yourself, perhaps because you don't want to have Yet Another E-mail.

Being the nerd you truly are, you set up a local HTTPS server in your LAN to save URLs and list them on a web page:

![Screenshot](/screenshot.png?raw=true "How it looks like")

## Installation:

(as the uwsgi user, if not existing create one)

1.  Check out this repository
1. Set up a virtualenv in this directory: `virtualenv venv`
1. Activate the virtualenv: `source venv/bin/activate`
1. Install requirements: `pip install -r requirements.txt`

My recommendation is to put this package in a directory not under your webserver default (e.g. `/var/uwsgi`, not `/var/www`). For example, you could make `/var/uwsgi` the HOME for user uwsgi. There's an example for OpenBSD's `httpd` configuration.

## Use:

1. (as root) `uwsgi --ini uwsgi.ini`
2. Tell your webserver to speak FastCGI to port 3031 for urls starting with 'urlsh' (see example httpd.conf for OpenBSD's httpd)
3. Go to `http://your_ip/urlsh/`

There is no authentication in this app. Use your webserver to do so. Also, consider using https if possible.

## Development:

1. `source venv/bin/activate`
1. `python url_share.py`

## To change URL:

1. Edit `url_share.py`, change `urlsh` into your URL
2. Tell your webserver to speak FastCGI for that URL
