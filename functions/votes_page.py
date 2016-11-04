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


def count_vote(site_id, user_id, user_votes):
    update_user_vote_for_site(user_id, site_id, user_votes)
    return


def update_user_vote_for_site(site_id, user_id, user_votes):
    user_votes = int(user_votes) + 1
    sqlite_conn = SqliteConn()
    sql_query = USER_VOTE_FOR_SITE
    params = [
        site_id,
        user_votes,
        user_id,
    ]
    sqlite_conn.user_vote(sql_query, params)
    return


def update_site_vote_by_user(user_id, site_id):
    return
