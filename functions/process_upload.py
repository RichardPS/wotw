# PROCESS SCREENSHOT

# system
import os

# 3rd party
from PIL import Image
from slugify import slugify

# local
from config.app_config import SCREENSHOT_FOLDER
from config.app_config import TMP_FOLDER
from functions.global_functions import return_timestamp
from functions.sqlite_connection import SqliteConn
from functions.sql_queries import INSERT_NEW_SITE


def process_new_screenshot(file_name):
    ''' set path to uploaded screenshot '''
    file, ext = os.path.splitext(TMP_FOLDER + '/' + file_name)
    ''' open image '''
    img = Image.open(TMP_FOLDER + '/' + file_name)
    ''' set maximium dimentions of thumbnail '''
    maxsize = 250, 250
    ''' resize image '''
    img.thumbnail(maxsize, Image.ANTIALIAS)
    ''' get timestamp to append to filename '''
    append_name = str(return_timestamp())
    ''' generate new file name '''
    new_file_name = append_name + file_name
    ''' save thumbnail '''
    img.save(SCREENSHOT_FOLDER + new_file_name, 'JPEG')
    ''' remove image in tmp folder '''
    os.remove(TMP_FOLDER + '/' + file_name)
    return new_file_name


def slugify_file_name(file_name):
    sluged_file_name = slugify(file_name, to_lower=True)
    return sluged_file_name


def add_upload_details_to_db(
        return_timestamp,
        school_name,
        website_url,
        designer_name,
        launch_date,
        new_file_name
        ):
    sqlite_conn = SqliteConn()
    sql_query = INSERT_NEW_SITE.format(
        return_timestamp,
        school_name,
        website_url,
        designer_name,
        launch_date,
        new_file_name
        )
    print sql_query
    sqlite_conn.add_new_site(sql_query)
    return
