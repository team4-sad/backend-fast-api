from dotenv import dotenv_values


class Config:
    def __init__(self, path_env: str = ".env"):
        self._config = dotenv_values(path_env)

    @property
    def base_singular_news(self):
        return self._config['BASE_SINGULAR_NEWS']

    @property
    def base_news_list_url(self):
        return self._config['BASE_NEWS_LIST_URL']

    @property
    def base_link_url(self):
        return self._config['BASE_LINK_URL']

    @property
    def port(self):
        return int(self._config['PORT'])

    @property
    def database_path(self):
        return self._config['DATABASE_PATH']

    @property
    def base_schedule_api_url(self):
        return self._config['BASE_SCHEDULE_API_URL']
