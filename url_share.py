"""
A simple url-sharing app across a network.

Use: from a browser, paste an URL in the form. The URL will be saved
in-memory. Then from another browser access the same page and retrieve the
URL.

Alternative use: perform a HTTP POST from a command-line tool like curl
invoked e.g. from a terminal mail client like mutt, and open the URL on
another computer.
"""

import argparse

from flask import Flask, request, render_template, url_for
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware


app = Flask(__name__)
app.config['APPLICATION_ROOT'] = '/urlsh'

urls = list()


def store_url(req):
    _url_data = req.args
    _form_data = req.form
    if _form_data:
        # as application/x-www-form-urlencoded
        for _k, _v in _form_data.items():
            if _k == 'url' and _v:
                urls.append(_v)
            elif _k != 'url' and not _v:
                urls.append(_k)
            else:
                # empty url
                continue
    if _url_data:
        _url = _url_data.get('url')
        if _url:
            urls.append(_url)


@app.route('/', methods=['GET', 'POST'])
def share_url():
    print url_for('share_url')
    if request.method == 'POST':
        store_url(request)

    return return_all()


def return_all():
    # return the list, reversed
    return render_template('shared_urls.html', urls=urls[::-1])


@app.route('/clean', methods=['POST'])
def cleanup():
    global urls
    urls = []
    return return_all()


# using a catch-all so I can deploy this behind a fixed url (e.g. /urlsh/)
# @app.route('/', methods=['GET', 'POST'], defaults={'path': ''})
# @app.route('/<path:path>', methods=['GET', 'POST'])
# def catch_all(path):
#         return 'You want path: %s' % path
def simple(env, resp):
    resp(b'200 OK', [(b'Content-Type', b'text/plain')])
    return [b'Hello WSGI World']

# point uwsgi/gunicorn/etc at this
parent_app = DispatcherMiddleware(simple, {'/abc/123': app})

# or run the dev server
if __name__ == '__main__':
    run_simple('localhost', 5000, parent_app)

# if __name__ == '__main__':
#     p = argparse.ArgumentParser()
#     p.add_argument('-d', '--debug', action='store_true')
#     args = p.parse_args()
#     if args.debug:
#         app.debug = True
#     app.run()
