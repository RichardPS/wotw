# -*- coding: utf-8 -*-

from functions.sqlite_connection import SqliteConn
from functions.sql_queries import SITE_VOTE_BY_USER
from functions.sql_queries import USER_VOTE_FOR_SITE
from functions.sql_queries import VOTERS_PAGE_QUERY

def wotw_voters():
    voters_dict = query_sqlite_voters()
    return voters_dict


def query_sqlite_voters():
    sqlite_conn = SqliteConn()
    sql_query = VOTERS_PAGE_QUERY
    rows = sqlite_conn.query(sql_query)
    return rows


def count_vote(user_id, site_uid, user_votes, site_votes):
    update_user_vote_for_site(user_id, site_uid, user_votes)
    update_site_vote_by_user(site_uid, site_votes)
    return


def update_user_vote_for_site(site_uid, user_id, user_votes):
    user_votes = int(user_votes) + 1
    sqlite_conn = SqliteConn()
    sql_query = USER_VOTE_FOR_SITE
    params = [
        site_uid,
        user_votes,
        user_id,
    ]
    sqlite_conn.user_vote(sql_query, params)
    return


def update_site_vote_by_user(site_uid, site_votes):
    site_votes = int(site_votes) + 1
    site_uid = int(site_uid)
    sqlite_conn = SqliteConn()
    sql_query = SITE_VOTE_BY_USER
    params = [
        site_votes,
        site_uid,
    ]
    print sql_query
    print params
    sqlite_conn.site_vote(sql_query, params)
    return
