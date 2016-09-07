# -*- coding: utf-8 -*-

from bottle import route
from bottle import run

from functions.screenshots import process_sites

@route('/')
def root():
    return 'Front Page'


@route('/admin')
def admin():
    return 'Admin Page'


@route('/view-users')
def view_users():
    return 'View Users'

@route('/view-sites')
def view_sites():
    return 'View Sites'


process_sites()

#run(host='0.0.0.0', port=8080, debug=True)
