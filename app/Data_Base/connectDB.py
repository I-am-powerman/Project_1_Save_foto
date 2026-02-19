from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class GetEngineSessionDB:
    def __init__(self, path_db: str, echo: bool = False) -> None:
        self.path_db = path_db
        self.echo = echo
        self._engine = None
        self._session_factory = None

    def get_engine(self):
        if self._engine is None:
            path = 'sqlite:///' + self.path_db
            self._engine = create_engine(path, echo=self.echo)
        return self._engine

    def get_session_factory(self):
        if self._session_factory is None:
            Session = sessionmaker(bind=self.get_engine())
            self._session_factory = Session
        return self._session_factory

    def get_session(self):
        """Возвращает новую сессию. Вызывающая сторона должна закрыть сессию."""
        Session = self.get_session_factory()
        return Session()