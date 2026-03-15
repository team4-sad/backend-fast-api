import os

from dotenv import dotenv_values


class Config:
    def __init__(self, path_env: str = ".env", is_relative_path: bool = True):
        if is_relative_path:
            project_dir = os.path.abspath(os.curdir)
            if "test" in project_dir:
                project_dir = project_dir.replace("\\test", "\\")
            path_env = os.path.join(project_dir, path_env)
        if not os.path.exists(path_env):
            raise FileNotFoundError(f"Config file not found: {path_env}")
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
