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
    lastname    TEXT    NOT NULL,
    firstname   TEXT    NOT NULL,
    patronymic  TEXT    NOT NULL,
    search_name TEXT    NOT NULL,
    CONSTRAINT teachers_pk PRIMARY KEY (id)
);"""


SEARCH_TEACHERS_SQL = """
select * from "teachers" where "search_name" like '%' || ? || '%'
"""

CREATE_TABLE_CLASSROOMS_SQL = """CREATE TABLE IF NOT EXISTS classrooms
(
    id   INTEGER NOT NULL,
    name TEXT    NOT NULL,
    CONSTRAINT teachers_pk PRIMARY KEY (id)
);
"""

SEARCH_CLASSROOM_SQL = """
    SELECT *
    FROM classrooms 
    WHERE "name" like '%' || ? || '%'
"""


CREATE_TABLE_LESSONS_SQL = """CREATE TABLE IF NOT EXISTS lessons
(
    id           TEXT    NOT NULL,
    classroom_id INTEGER NOT NULL,
    day_of_week  INTEGER NOT NULL,
    week_type    INTEGER NOT NULL,
    subject      TEXT    NOT NULL,
    lesson_type  TEXT    NOT NULL,
    CONSTRAINT lessons_pk PRIMARY KEY (id)
);"""


CREATE_TABLE_LESSON_TO_GROUPS_SQL = """CREATE TABLE IF NOT EXISTS lesson_to_groups(
    id        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_lesson TEXT NOT NULL,
    id_group  INTEGER NOT NULL,
    subgroup  TEXT
);"""


CREATE_TABLE_LESSON_TO_TEACHERS_SQL = """CREATE TABLE IF NOT EXISTS lesson_to_teachers
(
    id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_lesson  TEXT NOT NULL,
    id_teacher INTEGER NOT NULL
);"""


SEARCH_LESSONS_SQL = """
select * from "lessons" where "subject" like '%' || ? || '%'
"""