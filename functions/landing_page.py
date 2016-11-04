# -*- coding: utf-8 -*-

# root page elements
''' get website data from sqlite db for last weeks launches '''
''' dummy DB data, will be stored on sqlite db '''
db_site_data = [
    {'school-name': 'St Peter', 'designer-name': 'Mark Roe', 'site-thumb': 'st-peter.jpg', 'site-id': 1234, 'site-votes': 1,},
    {'school-name': 'St John', 'designer-name': 'Karl Fry', 'site-thumb': 'st-john.jpg', 'site-id': 1235, 'site-votes': 5,},
    {'school-name': 'St Mary', 'designer-name': 'Zoe Coultan', 'site-thumb': 'st-mary.jpg', 'site-id': 1236, 'site-votes': 3,},
    {'school-name': 'St Paul', 'designer-name': 'Joel Watkins-Groves', 'site-thumb': 'st-paul.jpg', 'site-id': 1237, 'site-votes': 7,},
]


def wotw_sites():
    ''' populate elements for page '''
    site_data = db_site_data
    return site_data


# iframe/fancybox elements to alolow voting
''' variable from vote request (user/site IDs) '''


''' update sitesql with votes for site and user '''


''' return and redirect back to root page '''
