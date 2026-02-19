from .connectDB import GetEngineSessionDB
from .model import Foto, Base
from typing import Optional, List


class WorkDB:
    """Класс для работы с базой данных фото."""

    def __init__(self, path_db: str, echo: bool = False) -> None:
        self.path_db = path_db
        self.db_connector = GetEngineSessionDB(path_db, echo)
        self._init_db()

    def _init_db(self):
        """Создаёт таблицы БД, если они не существуют."""
        engine = self.db_connector.get_engine()
        Base.metadata.create_all(engine)

    def add_foto(self, name_foto: str, path: str) -> Foto:
        """Добавляет запись о фото в БД."""
        session = self.db_connector.get_session()
        try:
            foto = Foto(name_foto=name_foto, path=path)
            session.add(foto)
            session.commit()
            session.refresh(foto)
            return foto
        finally:
            session.close()

    def get_foto_by_id(self, foto_id: int) -> Optional[Foto]:
        """Получает фото по ID."""
        session = self.db_connector.get_session()
        try:
            return session.query(Foto).filter(Foto.id == foto_id).first()
        finally:
            session.close()

    def get_all_fotos(self) -> List[Foto]:
        """Получает все записи из БД."""
        session = self.db_connector.get_session()
        try:
            return session.query(Foto).all()
        finally:
            session.close()

    def get_foto_by_name(self, name_foto: str) -> Optional[Foto]:
        """Получает фото по имени."""
        session = self.db_connector.get_session()
        try:
            return session.query(Foto).filter(Foto.name_foto == name_foto).first()
        finally:
            session.close()

    def delete_foto(self, foto_id: int) -> bool:
        """Удаляет фото по ID. Возвращает True, если удаление успешно."""
        session = self.db_connector.get_session()
        try:
            foto = session.query(Foto).filter(Foto.id == foto_id).first()
            if foto:
                session.delete(foto)
                session.commit()
                return True
            return False
        finally:
            session.close()
