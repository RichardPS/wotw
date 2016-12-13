# -*- coding: utf-8 -*-

# system
from datetime import datetime
from datetime import timedelta

# Local
from functions.mssql_connection import MsDbConn
from functions.screenshots import process_sites
from functions.sqlite_connection import SqliteConn
from functions.sql_queries import ALL_ACTIVE_USERS_QUERY
from functions.sql_queries import ARCHIVE_CURRENT_SITES
from functions.sql_queries import GET_NEW_SITES
from functions.sql_queries import SET_SITE_WINNER
from functions.sql_queries import SITE_INFO_QUERY
from functions.sql_queries import SITE_WINNERS_QUERY

def current_sites():
    ''' populate list dict of site info for landing page '''
    results = query_db_for_live_sites()
    site_data = add_keynames_from_results(results)
    return site_data


def query_db_for_live_sites():
    ''' query sqlite db for launched sites '''
    sqlite_conn = SqliteConn()
    sql_query = SITE_INFO_QUERY
    rows = sqlite_conn.query(sql_query)
    return rows


def add_keynames_from_results(sites_tuple):
    ''' convert tuple to dict '''
    sites_dict = []
    keys = ('school-name', 'designer-name', 'site-thumb', 'site-uid', 'site-votes', 'site-url')
    for item in sites_tuple:
        output = dict(zip(keys, item))
        sites_dict.append(output)
    return sites_dict


def get_current_total_votes(site_data):
    total_votes = 0
    for item in site_data:
        total_votes = total_votes + item['site-votes']
    return total_votes


def site_archive():
    ''' get current sites for archiving '''
    results = query_db_for_live_sites()
    site_data = add_keynames_from_results(results)
    return site_data


def archive_current_sites(winner):
    ''' create DB object '''
    sqlite_conn = SqliteConn()
    ''' archive current sites '''
    sql_archive_query = ARCHIVE_CURRENT_SITES
    sqlite_conn.archive(sql_archive_query)
    ''' set winner of current sites based on highest vote '''
    params = [winner]
    ''' get sql query '''
    sql_winner_query = SET_SITE_WINNER
    ''' update sqlite db '''
    sqlite_conn.set_winner(sql_winner_query, params)


def get_new_sites(date):
    ''' get date from date str '''
    monday_date = datetime.strptime(date, '%Y-%m-%d')
    ''' get next sundays date from mondays date '''
    sunday_date = monday_date + timedelta(days=6)
    ''' create MS DB Object '''
    msql_conn = MsDbConn()
    ''' generate sql query '''
    new_site_query = GET_NEW_SITES.format(monday_date, sunday_date)
    ''' query database '''
    new_site_results = msql_conn.query(new_site_query)
    ''' call function to add results to sqlite db '''
    insert_new_sites_to_sqlite(new_site_results)

def insert_new_sites_to_sqlite(new_site_results):
    ''' send new sites for screenhots and image processing '''
    for item in new_site_results:
        process_sites(item)
    return


def get_site_winners():
    results = query_site_winners()
    site_data = add_keynames_from_winner_results(results)
    return site_data


def add_keynames_from_winner_results(sites_tuple):
    ''' convert tuple to dict '''
    sites_dict = []
    keys = ('school-name', 'designer-name', 'site-thumb', 'site-uid', 'site-votes', 'site-url', 'launch-date')
    for item in sites_tuple:
        output = dict(zip(keys, item))
        sites_dict.append(output)
    return sites_dict


def query_site_winners():
    ''' query sqlite db for site winners '''
    sqlite_conn = SqliteConn()
    sql_query = SITE_WINNERS_QUERY
    rows = sqlite_conn.query(sql_query)
    return rows


def view_active_users():
    results = query_active_users()
    user_data = add_user_keynames(results)
    return user_data


def query_active_users():
    sqlite_conn = SqliteConn()
    sql_query = ALL_ACTIVE_USERS_QUERY
    rows = sqlite_conn.query(sql_query)
    return rows

def add_user_keynames(user_tuple):
    user_dict = []
    keys = ('user_firstname', 'user_surname', 'user_total_votes', 'user_id')
    for item in user_tuple:
        output = dict(zip(keys, item))
        user_dict.append(output)
    return user_dict


def admin_nav():
    navigation = """
        <section class='admin-nav'>
            <ul>
                <li><a href="/admin">Current Sites</a></li>
                <li><a href="/view-site-winners">Site Winners</a></li>
                <li><a href="/view-users">View Users</a></li>
                <li><a href="/add-user">Add User</a></li>
            </ul>
        </section>
    """
    return navigation
