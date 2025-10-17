CREATE_TABLE_NEWS_SQL = """CREATE TABLE news
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
    ORDER BY date DESC 
    LIMIT ? OFFSET ?
"""

GET_COUNT_NEWS_SQL = """
    SELECT COUNT(*) as total_count
    FROM news 
    WHERE search_header LIKE '%' || ? || '%'
"""