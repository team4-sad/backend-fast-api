CREATE_TABLE_NEWS_SQL = """CREATE TABLE news
(
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    header      TEXT    NOT NULL,
    date        TEXT    NOT NULL,
    link        TEXT    NOT NULL,
    cover_url   TEXT,
    description TEXT,
    news_id     INTEGER NOT NULL
);
"""

# offset = (page - 1) * page_size - сколько новостей нужно пропустить (были на прошлых страницах)
# limit - кол-во новостей на странице пагинации
SEARCH_NEWS_SQL = """
    SELECT * 
    FROM news 
    WHERE header LIKE '%' || ? || '%' 
    ORDER BY date DESC 
    LIMIT ? OFFSET ?
"""