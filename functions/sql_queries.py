# -*- coding: utf-8 -*-

''' SQLITE QUERIES '''
SITE_INFO_QUERY = """
  SELECT site_name, site_designer, site_thumb, site_uid, site_votes, site_url
  FROM sites
  WHERE site_archived IS NULL
  ORDER BY site_votes DESC
"""

LANDING_PAGE_QUERY = """
  SELECT site_name, site_designer, site_thumb, site_uid, site_votes, site_url
  FROM sites
  WHERE site_archived IS NULL
  ORDER BY site_name DESC
"""

SITE_WINNERS_QUERY = """
  SELECT site_name, site_designer, site_thumb, site_uid, site_votes, site_url, site_launch_date
  FROM sites
  WHERE site_week_winner IS NOT NULL
"""

VOTERS_PAGE_QUERY = """
  SELECT user_id, user_firstname, user_surname, user_username, user_total_votes
  FROM users
  WHERE user_active = 'True'
  AND user_voted_for_site_uid IS NULL;
"""

ALL_ACTIVE_USERS_QUERY = """
  SELECT user_firstname, user_surname, user_total_votes, user_id
  FROM users
  WHERE user_active = 'True'
  ORDER BY user_surname
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

ARCHIVE_CURRENT_SITES = """
  UPDATE sites
  SET site_archived = 1
  WHERE site_archived IS NULL
"""

SET_SITE_WINNER = """
  UPDATE sites
  SET site_week_winner = 1
  WHERE site_uid = ?
"""

INSERT_NEW_SITE = """
  INSERT INTO sites (site_act_id, site_name, site_url, site_designer, site_launch_date, site_votes, site_thumb)
  VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', 0, '{5}')
"""

ADD_USER_QUERY = """
  INSERT INTO users (user_username, user_firstname, user_surname, user_active, user_admin, user_total_votes, user_voted_for_site_uid)
  VALUES ('{0}', '{1}', '{2}', 'True', 'False', 0, NULL)
"""

DEACTIVATE_USER = """
  UPDATE users
  SET user_active = 'False'
  WHERE user_id = ?
"""

''' MSQL QUERIES '''
GET_NEW_SITES = """
SELECT
  TBL_CONTACT.COMPANYNAME AS LaunchName,
  TBL_CONTACT.CUST_HostingRenewalDate_082526703 AS LaunchDate,
  CUST_ContactTable2_121505.CUST_DesignerName_080640364 AS DesignerName,
  CUST_ContactTable2_121505.CUST_Secureaddress_080649505 AS URL,
  CAST(TBL_CONTACT.CONTACTID AS VARCHAR(50)) AS ActId
FROM dbo.CUST_ContactTable1_110237
INNER JOIN dbo.TBL_CONTACT
  ON CUST_ContactTable1_110237.CONTACTID = TBL_CONTACT.CONTACTID
INNER JOIN dbo.CUST_ContactTable2_121505
  ON CUST_ContactTable2_121505.CONTACTID = TBL_CONTACT.CONTACTID
INNER JOIN dbo.CUST_ContactTable3_052413
  ON CUST_ContactTable3_052413.CONTACTID = TBL_CONTACT.CONTACTID
WHERE TBL_CONTACT.CUST_HostingRenewalDate_082526703 BETWEEN '{0}' AND '{1}'
AND CUST_ContactTable2_121505.CUST_1stWebsiteStatus_051850534 IN ('Green', 'Adapted', 'Related', 'Returning Website')
UNION
SELECT
  TBL_CONTACT.COMPANYNAME AS LaunchName,
  CUST_ContactTable1_110237.CUST_2ndWebsiteLaunched_082613578 AS LaunchDate,
  CUST_ContactTable2_121505.CUST_2ndwebsiteDesignersName_080828292 AS DesignerName,
  CUST_ContactTable2_121505.CUST_2ndWebsiteSecureAddress_080715656 AS URL,
  CAST(TBL_CONTACT.CONTACTID AS VARCHAR(50)) AS ActId
FROM dbo.CUST_ContactTable1_110237
INNER JOIN dbo.TBL_CONTACT
  ON CUST_ContactTable1_110237.CONTACTID = TBL_CONTACT.CONTACTID
INNER JOIN dbo.CUST_ContactTable2_121505
  ON CUST_ContactTable2_121505.CONTACTID = TBL_CONTACT.CONTACTID
INNER JOIN dbo.CUST_ContactTable3_052413
  ON CUST_ContactTable3_052413.CONTACTID = TBL_CONTACT.CONTACTID
WHERE CUST_ContactTable1_110237.CUST_2ndWebsiteLaunched_082613578 BETWEEN '{0}' AND '{1}'
AND CUST_ContactTable1_110237.CUST_2ndWebsiteStatus_081938953 IN ('Green', 'Adapted', 'Related', 'Returning Website')
UNION
SELECT
  TBL_CONTACT.COMPANYNAME AS LaunchName,
  CUST_ContactTable1_110237.CUST_3rdWebsiteLaunched_124604005 AS LaunchDate,
  CUST_ContactTable2_121505.CUST_3rdWebsiteDesignersName_081042005 AS DesignerName,
  CUST_ContactTable2_121505.CUST_3rdWebsiteSecureAddress_051454526 AS URL,
  CAST(TBL_CONTACT.CONTACTID AS VARCHAR(50)) AS ActId
FROM dbo.CUST_ContactTable1_110237
INNER JOIN dbo.TBL_CONTACT
  ON CUST_ContactTable1_110237.CONTACTID = TBL_CONTACT.CONTACTID
INNER JOIN dbo.CUST_ContactTable2_121505
  ON CUST_ContactTable2_121505.CONTACTID = TBL_CONTACT.CONTACTID
INNER JOIN dbo.CUST_ContactTable3_052413
  ON CUST_ContactTable3_052413.CONTACTID = TBL_CONTACT.CONTACTID
WHERE CUST_ContactTable1_110237.CUST_3rdWebsiteLaunched_124604005 BETWEEN '{0}' AND '{1}'
AND CUST_ContactTable2_121505.CUST_3rdWebsiteStats_083327489 IN ('Green', 'Adapted', 'Related', 'Returning Website')
UNION
SELECT
  TBL_CONTACT.COMPANYNAME AS LaunchName,
  CUST_ContactTable2_121505.CUST_4thWebsiteLaunched_052322301 AS LaunchDate,
  CUST_ContactTable2_121505.CUST_4thWebsiteDesigner_052230157 AS DesignerName,
  CUST_ContactTable3_052413.CUST_4thWebsiteSecureAddress_052413772 AS URL,
  CAST(TBL_CONTACT.CONTACTID AS VARCHAR(50)) AS ActId
FROM dbo.CUST_ContactTable1_110237
INNER JOIN dbo.TBL_CONTACT
  ON CUST_ContactTable1_110237.CONTACTID = TBL_CONTACT.CONTACTID
INNER JOIN dbo.CUST_ContactTable2_121505
  ON CUST_ContactTable2_121505.CONTACTID = TBL_CONTACT.CONTACTID
INNER JOIN dbo.CUST_ContactTable3_052413
  ON CUST_ContactTable3_052413.CONTACTID = TBL_CONTACT.CONTACTID
WHERE CUST_ContactTable2_121505.CUST_4thWebsiteLaunched_052322301 BETWEEN '{0}' AND '{1}'
AND CUST_ContactTable3_052413.CUST_4thWebsiteStatus_052547793 IN ('Green', 'Adapted', 'Related', 'Returning Website')
"""
