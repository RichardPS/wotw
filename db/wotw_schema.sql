--
-- File generated with SQLiteStudio v3.1.0 on Tue Sep 6 22:21:41 2016
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: sites
DROP TABLE IF EXISTS sites;

CREATE TABLE sites (
    site_uid         INTEGER       PRIMARY KEY AUTOINCREMENT
                                   REFERENCES users (user_voted_for_site_uid),
    site_act_id      INTEGER,
    site_name        VARCHAR (255),
    site_url         VARCHAR (255),
    site_designer    VARCHAR (100),
    site_launch_date DATE,
    site_votes       INTEGER,
    site_week_winner BOOLEAN,
    site_archived    BOOLEAN
);


-- Table: users
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id                 INTEGER       PRIMARY KEY AUTOINCREMENT,
    user_username           VARCHAR (100),
    user_firstname          VARCHAR (100),
    user_surname            VARCHAR (100),
    user_active             BOOLEAN,
    user_admin              BOOLEAN,
    user_total_votes        INTEGER,
    user_voted_for_site_uid INTEGER
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
