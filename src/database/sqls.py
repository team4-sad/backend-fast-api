CREATE_TABLE_NEWS_SQL = """CREATE TABLE IF NOT EXISTS news
(
    id              INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    header          TEXT    NOT NULL,
    date            TEXT    NOT NULL,
    link            TEXT    NOT NULL,
    cover_url       TEXT,
    description     TEXT,
    news_id         INTEGER NOT NULL, 
    search_header   TEXT
);

CREATE INDEX idx_news_search_header ON news(search_header);
"""

# offset = (page - 1) * page_size - сколько новостей нужно пропустить (были на прошлых страницах)
# limit - кол-во новостей на странице пагинации
SEARCH_NEWS_SQL = """
    SELECT * 
    FROM news 
    WHERE search_header LIKE '%' || LOWER(?) || '%'
    ORDER BY strftime('%Y-%m-%d', substr(date, 7, 4) || '-' || substr(date, 4, 2) || '-' || substr(date, 1, 2)) DESC
    LIMIT ? OFFSET ?
"""

GET_COUNT_NEWS_SQL = """
    SELECT COUNT(*) as total_count
    FROM news 
    WHERE search_header LIKE '%' || LOWER(?) || '%'
"""

GET_DATE_NEWS_SQL = """
    SELECT * 
    FROM news 
    WHERE date = ?;
"""

GET_LAST_NEWS_SQL = """
    SELECT *
    FROM news
    ORDER BY strftime('%Y-%m-%d', substr(date, 7, 4) || '-' || substr(date, 4, 2) || '-' || substr(date, 1, 2)) DESC
    LIMIT 1;
"""

CREATE_TABLE_GROUPS_SQL = """CREATE TABLE IF NOT EXISTS groups
(
    id         INTEGER NOT NULL,
    name       TEXT    NOT NULL,
    "year"     INTEGER NOT NULL,
    faculty    TEXT    NOT NULL,
    department TEXT    NOT NULL,
    "group"    TEXT    NOT NULL,
    CONSTRAINT groups_pk PRIMARY KEY (id)
);"""

SEARCH_GROUPS_SQL = """
select * from "groups" where "name" like '%' || ? || '%'
"""


CREATE_TABLE_TEACHERS_SQL = """CREATE TABLE IF NOT EXISTS teachers
(
	id          INTEGER NOT NULL,
	lastname    TEXT NOT NULL,
	firstname   TEXT NOT NULL,
	patronymic  TEXT NOT NULL,
	search_name TEXT NOT NULL,
	CONSTRAINT  teachers_pk PRIMARY KEY (id)
);"""


SEARCH_TEACHERS_SQL = """
select * from "teachers" where "search_name" like '%' || ? || '%'
"""
