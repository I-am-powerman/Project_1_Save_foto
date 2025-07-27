import psycopg2

class driver_sql:
    def __init__(self, name_DB: str, user_name: str):
        self.conn = self._connect_DB(name_DB, user_name)

    def _connect_DB(self, name_DB, user_name):
        conn = psycopg2.connect(dbname=name_DB, 
                                host="localhost", 
                                user=user_name, 
                                password="d13031998", 
                                port="5432")

        return conn

    def insert_sql(self, name_table: str, name_columns: str, values: list):
        protect_value = ""
        counter = 0

        while 1:
            if  len(values) != counter:
                protect_value += "%s"
                if len(values) - 1 != counter:
                    protect_value += ", "
                counter += 1
            else:
                break
        
        insert_sql = f"INSERT INTO {name_table}({name_columns}) VALUES ({protect_value});"
        values_sql = values
        self.conn.cursor().execute(insert_sql, values_sql)
        self.conn.commit()
    
    def close_DB(self):
        self.conn.cursor().close()
        self.conn.close()