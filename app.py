# -*- coding: utf-8 -*-

# 3rd party
from bottle import get
from bottle import redirect
from bottle import request
from bottle import route
from bottle import run
from bottle import static_file
from bottle import view

#local
from config.app_config import TMP_FOLDER
from functions.admin_home import add_user_to_db
from functions.admin_home import admin_nav
from functions.admin_home import archive_current_sites
from functions.admin_home import deactivate_user_profile
from functions.admin_home import site_archive
from functions.admin_home import current_sites
from functions.admin_home import get_current_total_votes
from functions.admin_home import get_site_winners
from functions.admin_home import get_new_sites
from functions.admin_home import view_active_users
from functions.global_functions import return_timestamp
from functions.landing_page import get_total_votes
from functions.landing_page import wotw_sites
from functions.process_upload import add_upload_details_to_db
from functions.process_upload import process_new_screenshot
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
    ''' display current sites '''
    site_data = current_sites()
    navigation = admin_nav()
    current_total_votes = get_current_total_votes(site_data)
    return dict(
        site_data = site_data,
        current_total_votes = current_total_votes,
        navigation = navigation
        )


@route('/archive')
@view('archive')
def archive():
    ''' display sites that will be archived '''
    site_data = site_archive()
    winner = site_data[0]
    return dict(site_data = site_data, winner = winner)


@route('/continue-archive', method='POST')
def continue_archive():
    ''' archive sites and set this weeks winner '''
    winner = request.forms.get('winner')
    ''' archive current sites '''
    archive_current_sites(winner)
    redirect('/admin')



@route('/admin-add-site')
@view('admin-add-site')
def admin_add():
    navigation = admin_nav()
    return dict(navigation = navigation)


@route('/upload-new-site', method='POST')
def upload_new_site():
    ''' get form data '''
    school_name = request.forms.get('school_name')
    website_url = request.forms.get('website_url')
    designer_name = request.forms.get('designer_name')
    launch_date = request.forms.get("launch_date")
    website_screenshot = request.files.get('website_screenshot')
    ''' get screenshot file name '''
    file_name = website_screenshot.filename
    ''' save im tmp folder '''
    website_screenshot.save(TMP_FOLDER)
    ''' process screenshot for thumbnail '''
    new_file_name = process_new_screenshot(file_name)
    ''' insert new upload details to sqlite db '''
    add_upload_details_to_db(
        return_timestamp(),
        school_name,
        website_url,
        designer_name,
        launch_date,
        new_file_name
        )
    redirect('/admin')


@route('/view-users')
@view('view-users')
def view_users():
    user_data = view_active_users()
    navigation = admin_nav()
    return dict(user_data = user_data, navigation = navigation)


@route('/remove-uers')
@view('remove-user')
def remove_user():
    user_id = request.forms.get('user_id')


@route('/add-user')
@view('add-user')
def add_user():
    navigation = admin_nav()
    return dict(navigation = navigation)


@route('/add-user-to-db', method='post')
def add_user():
    user_forname = request.forms.get('forname')
    user_surname = request.forms.get('surname')
    add_user_to_db(user_forname, user_surname)
    redirect('/view-users')

@route('/view-site-winners')
@view('view-site-winners')
def view_site_winners():
    site_data = get_site_winners()
    navigation = admin_nav()
    return dict(site_data = site_data, navigation = navigation)


@route('/deactivate-user', method='post')
def deactivate_user():
    user_id = request.forms.get('user_id')
    deactivate_user_profile(user_id)
    redirect('/view-users')

run(host='0.0.0.0', port=8080, debug=True, reloader=True)
