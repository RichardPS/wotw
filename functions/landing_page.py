# -*- coding: utf-8 -*-

# Local
from functions.sqlite_connection import SqliteConn
from functions.sql_queries import SITE_INFO_QUERY


''' get website data from sqlite db for last weeks launches '''
def wotw_sites():
    ''' populate lsit dict of site info for landing page '''
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


def get_total_votes(site_data):
    total_votes = 0
    for item in site_data:
        total_votes = total_votes + item['site-votes']
    return total_votes
