# -*- coding: utf-8 -*-

# 3rd party
import sqlite3

# local
from config.connection_constants import SQLITE_DATABASE


# sqlite connection
class SqliteConn(object):
    ''' local sqlite connection '''
    db_connection = None
    db_cur = None

    sqlite_database = SQLITE_DATABASE

    def __init__(self):
        ''' open connection and define cursor '''
        sqlite_database = self.sqlite_database
        self.db_connection = sqlite3.connect(sqlite_database)
        self.db_cur = self.db_connection.cursor()


    def query(self, sql_query):
        ''' execute submitted query '''
        self.db_cur.execute(sql_query)
        return self.db_cur.fetchall()


    def user_vote(self, sql_query, params):
        ''' user vote for site '''
        self.db_cur.execute(sql_query,
            (params[0], params[1], params[2]))
        self.db_connection.commit()


    def site_vote(self, sql_query, params):
        ''' site vote by user '''
        return
