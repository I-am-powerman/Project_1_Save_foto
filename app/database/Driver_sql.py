import psycopg2


class Driver_sql:
    def __init__(
        self, name_DB: str, name_host: str, user_name: str, password: str, port: str
    ):
        self.conn = self._connect_DB(name_DB, name_host, user_name, password, port)
        self.cur = self._cursor(self.conn)

    # подключение к базе данных, метод инициализируется в init
    # и передает параметр conn который используется в выполнении
    def _connect_DB(
        self, name_DB: str, name_host: str, user_name: str, password: str, port: str
    ):
        conn = psycopg2.connect(
            dbname=name_DB, host=name_host, user=user_name, password=password, port=port
        )

        return conn

    def _cursor(self, conn):
        cur = conn.cursor()

        return cur

    # функция выполненения SQL запроса
    # get_data нужен для SQL запроса на получение данных
    def perform_sql(self, SQL_request: str, dict_values: dict):

        self.cur.execute(SQL_request, dict_values)

    # теперь эта функция вытаскивает объект по названию параметра
    def get_data(self, SQL_request: str):
        self.cur.execute(SQL_request)
        date_dict = {}
        while data := self.cur.fetchone():
            date_dict[data[0]] = [data[0]]

        return date_dict

    # эта функция закрывает БД
    def close_DB(
        self,
    ):
        self.conn.commit()
        self.conn.cursor().close()
        self.conn.close()
