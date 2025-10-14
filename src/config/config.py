from dotenv import dotenv_values


class Config:
    def __init__(self, path_env: str = ".env"):
        self._config = dotenv_values(path_env)

    @property
    def BASE_SINGULAR_NEWS(self):
        return self._config['BASE_SINGULAR_NEWS']

    @property
    def BASE_NEWS_LIST_URL(self):
        return self._config['BASE_NEWS_LIST_URL']

    @property
    def BASE_LINK_URL(self):
        return self._config['BASE_LINK_URL']

    @property
    def PORT(self):
        return int(self._config['PORT'])
