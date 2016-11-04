# -*- coding: utf-8 -*-

from bottle import get
from bottle import redirect
from bottle import route
from bottle import run
from bottle import static_file
from bottle import view

#from functions.screenshots import process_sites
from functions.landing_page import wotw_sites
from functions.votes_page import wotw_voters
from functions.votes_page import count_vote

# Static Files Routes
@get('/<filename:re:.*\.js>')
def javascript(filename):
    """Static route for javascript."""
    return static_file(filename, root = 'static/js')


@get('/<filename:re:.*\.css>')
def stylesheet(filename):
    """Static route for stylesheets."""
    return static_file(filename, root = 'static/css')


@get('/<filename:re:.*\.(png|gif|ico)>')
def image(filename):
    """Static route for images."""
    return static_file(filename, root = 'static/images')


@get('/<filename:re:.*\.jpg>')
def image(filename):
    """Static route for images."""
    return static_file(filename, root = 'static/jpg')


@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def font(filename):
    """Static route for fonts."""
    return static_file(filename, root = 'static/fonts')


@get('/<filename:re:.*\.zip>')
def zip(filename):
    """Static route for zipped themes."""
    return static_file(filename, root = 'static/themezips')


@route('/')
@view('index')
def index():
    site_data = wotw_sites()
    return dict(site_data = site_data)

@route('/vote/<site_id>')
@view('vote')
def vote(site_id):
    voters = wotw_voters()
    return dict(site_id = site_id, voters = voters)

@route('/voted_for/<user_id>/<site_id>/<user_votes>')
def voted_for(user_id, site_id, user_votes):
    count_vote(user_id, site_id, user_votes)
    redirect('/')


@route('/admin')
def admin():
    return 'Admin Page'


@route('/view-users')
def view_users():
    return 'View Users'

@route('/view-sites')
def view_sites():
    return 'View Sites'


#process_sites()

run(host='0.0.0.0', port=8080, debug=True, reloader=True)
