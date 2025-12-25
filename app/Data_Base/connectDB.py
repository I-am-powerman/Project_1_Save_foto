from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Get_engine_session_DB():
    def __init__(self, path_DB:str) -> None:
        self.path_DB:str = path_DB
    
    def get_engine(self):
        path = 'sqlite:///' + self.path_DB

        return create_engine(path, echo=True)

    def get_sessoin(self):
        Session = sessionmaker(bind=self.get_engine())
        with Session() as session:
            return session