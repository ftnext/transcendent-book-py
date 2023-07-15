from abc import ABCMeta, abstractmethod


class Article:
    ...


class ArticleRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def fetch(self, id: str) -> Article:
        ...


class ArticlePresenterInterface(metaclass=ABCMeta):
    @abstractmethod
    def format(self, article: Article) -> str:
        ...


class ArticleOperation:
    def __init__(
        self,
        repository: ArticleRepositoryInterface,
        presenter: ArticlePresenterInterface,
    ) -> None:
        self.repository = repository
        self.presenter = presenter

    def show(self, id: str) -> str:
        article = self.repository.fetch(id)
        return self.presenter.format(article)


class ArticleRepository(ArticleRepositoryInterface):
    def fetch(self, id: str) -> Article:
        # TODO データベースに問い合わせる
        raise NotImplementedError


class ArticlePresenter(ArticlePresenterInterface):
    def format(self, article: Article) -> str:
        # TODO 表示用HTMLに整形する
        raise NotImplementedError


if __name__ == "__main__":
    operation = ArticleOperation(ArticleRepository(), ArticlePresenter())
    # operation.show("spam")
