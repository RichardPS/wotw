# -*- coding: utf-8 -*-


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

"""
