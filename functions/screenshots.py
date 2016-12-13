# -*- coding: utf-8 -*-

import os

from PIL import Image
from pyvirtualdisplay import Display
from selenium import webdriver
from slugify import slugify
from time import time

#temp site list as would be selected from ACT database
TEMP_SITES = [
    {
        'site_act_id': 1234,
        'site_name': 'St Johns',
        'site_url': 'https://eddie.secure-primarysite.net/',
        'site_designer': 'Mark Roe',
        'site_launch_date': '01/07/2016',
    },
    {
        'site_act_id': 1235,
        'site_name': 'St Marks',
        'site_url': 'https://richard.stage-primarysite.net/',
        'site_designer': 'Karl Fry',
        'site_launch_date': '05/07/2016',
    },
    {
        'site_act_id': 1236,
        'site_name': 'St Patricks',
        'site_url': 'https://demo.stage-primarysite.net/',
        'site_designer': 'Joe Blogs',
        'site_launch_date': '02/07/2016',
    },
    {
        'site_act_id': 1237,
        'site_name': 'St Marys',
        'site_url': 'https://dale.secure-primarysite.net/',
        'site_designer': 'Jane Doe',
        'site_launch_date': '03/07/2016',
    },
]



def take_screenshot(site_url, file_name):
    ''' take screenshot of website with virtualdisplay '''

    display = Display(visible=0, size=(1280, 1024))
    display.start()

    browser = webdriver.Firefox()
    browser.set_window_size(1280, 1024)
    browser.get(site_url)
    #browser.save_screenshot('tmp/{0}'.format(file_name))
    browser.save_screenshot('bob.jpg')

    ''' resize image '''
    #resize_image(file_name)

    browser.quit()
    display.stop()
    return


def generate_unique_filename(site_name, site_act_id):
    ''' generate unique filename for screenshot '''
    timestamp = str(int(time()))
    site_name = slugify(site_name, to_lower=True)
    site_act_id = str(site_act_id)
    file_name = '{0}-{1}-{2}.jpg'.format(
            site_name,
            site_act_id,
            timestamp
        )
    return file_name


def resize_image(file_name):
    ''' resize screenshot and overwrite oridinal '''
    file, ext = os.path.splitext("tmp/" + file_name)
    img = Image.open(file_name)
    maxsize = 400, 400
    img.thumbnail(maxsize, Image.ANTIALIAS)
    img.save(file_name, 'JPEG')
    return


def process_sites(new_site):
    ''' generate filename '''
    file_name = generate_unique_filename(
        new_site['LaunchName'],
        new_site['ActId']
    )
    print new_site['URL']
    print file_name
    ''' take screenshot '''
    take_screenshot(new_site['URL'], file_name)
    return file_name
