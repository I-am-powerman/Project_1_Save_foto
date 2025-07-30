import psycopg2

class driver_sql:
    def __init__(self, name_DB:str, name_host:str, user_name:str,
                     password: str, port:str):
        self.conn = self._connect_DB(name_DB, name_host, user_name,
                     password, port)

    # подключение к базе данных, метод инициализируется в init
    # и передает параметр conn который используется в выполнении
    def _connect_DB(self, name_DB:str, name_host:str, user_name:str,
                     password: str, port:str):
        conn = psycopg2.connect(dbname=name_DB, 
                                host=name_host, 
                                user=user_name, 
                                password=password, 
                                port=port)

        return conn

    # функция выполненения SQL запроса
    # get_data нужен для SQL запроса на получение данных
    def perform_sql(self, SQL_request: str, dict_values: dict = None, get_data: bool = False):

        self.conn.cursor().execute(SQL_request, dict_values)
        
        if get_data:
            # пока сделал чтобы он все данные доставал
            return self.conn.cursor().fetchall()
        
        self.conn.commit()
        self.conn.cursor().close()
        self.conn.close()