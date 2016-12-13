# -*- coding: utf-8 -*-

# 3rd-party
import pymssql

# local
from config.connection_constants import MSSQL_DATABASE
from config.connection_constants import MSSQL_PASSWORD
from config.connection_constants import MSSQL_SERVER
from config.connection_constants import MSSQL_USER

# mssql connection
class MsDbConn(object):
    ''' ACT MSSQL db connection '''
    _db_connection = None
    _db_cur = None

    mssql_database = MSSQL_DATABASE
    mssql_password = MSSQL_PASSWORD
    mssql_server = MSSQL_SERVER
    mssql_user = MSSQL_USER

    def __init__(self):
        ''' open connection and define cursor '''
        server = self.mssql_server
        user = self.mssql_user
        password = self.mssql_password
        database = self.mssql_database
        self._db_connection = pymssql.connect(
            server, user, password, database, as_dict=True
            )
        self._db_cur = self._db_connection.cursor()

    def query(self, sql_query):
        ''' execute query and return results (dictionary) '''
        self._db_cur.execute(sql_query)
        return self._db_cur.fetchall()

    def __del__(self):
        self._db_connection.close()
