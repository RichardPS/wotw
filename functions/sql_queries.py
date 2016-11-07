# -*- coding: utf-8 -*-

SITE_INFO_QUERY = """
    SELECT site_name, site_designer, site_thumb, site_uid, site_votes, site_url
    FROM sites
    WHERE site_archived IS NULL
"""

VOTERS_PAGE_QUERY = """
    SELECT user_id, user_firstname, user_surname, user_username, user_total_votes
    FROM users
    WHERE user_active = 'True'
    AND user_voted_for_site_uid IS NULL;
"""

USER_VOTE_FOR_SITE = """
    UPDATE users
    SET user_voted_for_site_uid = ?,
    user_total_votes = ?
    WHERE user_id = ?
"""

SITE_VOTE_BY_USER = """
    UPDATE sites
    SET site_votes = ?
    WHERE site_uid = ?
"""
