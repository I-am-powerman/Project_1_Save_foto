from driver_sql import *
from SQL_request import *
import password


work_table_1 = driver_sql("proba", "localhost", "postgres",
                             password.password_BD, "5432")
name_image = ["image_1"]
name_collumns = ["name_1"]

Query = SQL_request("table_1", name_collumns, name_image)

Query_1 = Query.req_insert()

work_table_1.perform_sql(Query_1)

Query_2_sql = Query.req_obtain()
Query_2_values = Query.dict_values

date = work_table_1.perform_sql(Query_2_sql, Query_2_values, True)

print(date)