# url-share
A simple web app to share URLs across a network

Installation:

(as the uwsgi user, if not existing create one)

1. Set up a virtualenv in this directory: virtualenv venv
1. Activate the virtualenv: source venv/bin/activate
1. Install requirements: pip install -r requirements.txt

My recommendation is to put this package in a directory not under your webserver default (e.g. /var/uwsgi, not /var/www). For example, you could make /var/uwsgi the HOME for user uwsgi.

Use:

1. (as root) uwsgi --ini uwsgi.ini
2. Tell your webserver to speak FastCGI to port 3031 for urls starting with 'urlsh' (see example httpd.conf for OpenBSD's httpd)
3. Go to http://your_ip/urlsh/

There is no authentication in this app. Use your webserver to do so. Also, consider using https if possible.

Development:

1. source venv/bin/activate
1. python url_share.py

To change URL:

1. Edit url_share.py, change 'urlsh' into your URL
2. Tell your webserver to speak FastCGI for that URL
