"""
A simple url-sharing app across a network.

Use: from a browser, paste an URL in the form. The URL will be saved
in-memory. Then from another browser access the same page and retrieve the
URL.

Alternative use: perform a HTTP POST from a command-line tool like curl
invoked e.g. from a terminal mail client like mutt, and open the URL on
another computer.

This page has no authentication; this is left to the web server.
"""

import argparse

from flask import Flask, request, render_template, url_for, redirect
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
    if request.method == 'POST':
        store_url(request)

    # return the list, reversed
    return render_template(
        'shared_urls.html',
        urls=urls[::-1],
        path=url_for('share_url'),
        cleanpath=url_for('cleanup'))


@app.route('/clean', methods=['GET', 'POST'])
def cleanup():
    if request.method == 'POST':
        global urls
        urls = []
    return redirect(url_for('share_url'))

# point uwsgi/gunicorn/etc at parent_app
parent_app = DispatcherMiddleware(Flask('urlshare'), {
    app.config['APPLICATION_ROOT']: app,
})

# for local development
# thanks to: https://gist.github.com/rduplain/1705072
# also: http://stackoverflow.com/a/18967744/204634
if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('-d', '--debug', action='store_true')
    args = p.parse_args()
    if args.debug:
        app.debug = True
    run_simple('localhost', 5000, parent_app, use_reloader='True')
