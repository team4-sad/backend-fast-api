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

CREATE INDEX IF NOT EXISTS idx_news_search_header ON news(search_header);
"""

CREATE_TABLE_SCHEDULES_SQL = """CREATE TABLE IF NOT EXISTS schedules
(
    id              INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    data            BLOB    NOT NULL UNIQUE,
    start_date      TEXT    NOT NULL,
    end_date        TEXT    NOT NULL,
    insertion_date  TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_schedules_start_date ON schedules(start_date);
CREATE INDEX IF NOT EXISTS idx_schedules_end_date ON schedules(end_date);
CREATE INDEX IF NOT EXISTS idx_schedules_dates_range ON schedules(start_date, end_date);
CREATE INDEX IF NOT EXISTS idx_schedules_insertion_date ON schedules(insertion_date DESC);
CREATE INDEX IF NOT EXISTS idx_schedules_data_hash ON schedules(data_hash);
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

GET_PAGINATED_NEWS_SQL = """
SELECT * FROM news 
ORDER BY date DESC 
LIMIT ? OFFSET ?
"""

GET_TOTAL_NEWS_COUNT_SQL = """
    SELECT COUNT(*) as total_count
    FROM news
"""
