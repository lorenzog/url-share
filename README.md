# url-share
A simple web app to share URLs across a network

Installation:

1. Set up a virtualenv in this directory: virtualenv venv
1. Activate the virtualenv: source venv/bin/activate
1. Install requirements: pip install -r requirements.txt
2. If necessary, edit uwsgi.ini to reflect the name of the virtualenv (defaults to 'venv')
3. If necessary, edit uwsgi.ini, specify the user to drop privileges to (defaults to 'www')

Use:

1. uwsgi --ini uwsgi.ini
2. Tell your webserver to speak FastCGI to port 3031 for urls starting with 'urlsh' (see example httpd.conf for OpenBSD's httpd)

Development:

1. source venv/bin/activate
1. python url_share.py

To change URL:

1. Edit url_share.py, change 'urlsh' into your URL
2. Tell your webserver to speak FastCGI for that URL
