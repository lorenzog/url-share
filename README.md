# url-share
A simple web app to share URLs across a network

Use:

1. Set up a virtualenv in this directory: virtualenv venv
1. Activate the virtualenv: source venv/bin/activate
1. Install requirements: pip install -r requirements.txt
2. Edit uwsgi.ini to reflect the name of the virtualenv (defaults to 'venv')
3. Edit uwsgi.ini, specify the user to drop privileges to (defaults to 'www')
