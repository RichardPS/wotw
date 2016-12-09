# -*- coding: utf-8 -*-

from bottle import get
from bottle import redirect
from bottle import request
from bottle import route
from bottle import run
from bottle import static_file
from bottle import view

#from functions.screenshots import process_sites
from functions.admin_home import current_sites
from functions.admin_home import get_current_total_votes
from functions.landing_page import get_total_votes
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

# PAGE URLS
@route('/')
@view('index')
def index():
    site_data = wotw_sites()
    total_votes = get_total_votes(site_data)
    return dict(site_data = site_data, total_votes = total_votes)

@route('/vote/<site_uid>/<site_votes>')
@view('vote')
def vote(site_uid, site_votes):
    voters = wotw_voters()
    return dict(site_uid = site_uid, voters = voters, site_votes = site_votes)

@route('/voted_for/<user_id>/<site_uid>/<user_votes>/<site_votes>')
def voted_for(user_id, site_uid, user_votes, site_votes):
    count_vote(user_id, site_uid, user_votes, site_votes)
    redirect('/')


@route('/admin')
@view('admin')
def admin():
    site_data = current_sites()
    current_total_votes = get_current_total_votes(site_data)
    return dict(site_data = site_data, current_total_votes = current_total_votes)


@route('/admin-add-site')
@view('admin-add-site')
def admin_add():
    return dict()

@route('/upload-new-site', method='POST')
def upload_new_site():
    school_name = request.forms.get('school_name')
    website_url = request.forms.get('website_url')
    designer_name = request.forms.get('designer_name')
    website_screenshot = request.files.get('website_screenshot')
    tmp_screenhot_path = 'tmp'
    website_screenshot.save(tmp_screenhot_path)
    return 'Upload'

@route('/view-users')
def view_users():
    return 'View Users'

@route('/view-sites')
def view_sites():
    return 'View Sites'


#process_sites()

run(host='0.0.0.0', port=8080, debug=True, reloader=True)
