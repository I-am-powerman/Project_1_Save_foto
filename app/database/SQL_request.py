from .Protect import Protect


class SQL_request:
    def __init__(self, _name_table: str, _name_columns: list, _values: list = []):
        self._name_table: str = _name_table
        self._name_columns: list = _name_columns
        self._values: list = _values
        self._str_colum = self._transf_columns(_name_columns)

    # формирует словарь из параметров для защиты ввода
    def dict_values(self) -> dict:
        protect_values = Protect(self._name_columns, self._values)

        return protect_values.dict_values

    # запрос на внесение данных в таблицу
    def req_insert(self) -> str:
        protect_values = Protect(self._name_columns, self._values)

        sql_req = f"INSERT INTO {self._name_table} ({self._str_colum}) VALUES ({(protect_values.keys_str)});"

        return sql_req

    # запрос на создание новой таблицы
    def cr_new_tab(self) -> str:

        sql_req = f"CREATE TABLE {self._name_table} ({self._str_colum});"

        return sql_req

    # запрос на получение данных как объектов
    def req_obtain(self) -> str:

        sql_req = f"SELECT {self._str_colum} FROM {self._name_table}"

        return sql_req
    # достать первое отсортированное значение по убыванию
    def limited(self) -> str:
        sql_req = f"SELECT {self._str_colum} FROM {self._name_table} ORDER BY id DESC LIMIT 1"

        return sql_req

    # изменяет список наименований колонок на str
    def _transf_columns(self, _name_columns: list) -> str:
        _str_collum = ",".join(_name_columns)

        return _str_collum
