import abc


class INewsRepository(abc.ABC):

    def get_news_list(self, page: int):
        pass

    def get_singular_news(self, news_id: int):
        pass
