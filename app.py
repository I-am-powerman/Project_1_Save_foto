from Driver_sql import *
from SQL_request import *
import password


work_table_1 = Driver_sql(
    "proba", "localhost", "postgres", password.password_BD, "5432"
)
name_image = ["image_5"]
name_collumns = ["name_1"]

Query = SQL_request("table_1", name_collumns, name_image)

Query_1_sql = Query.req_insert()
Query_1_values = Query.dict_values()
Query_2_sql = Query.req_obtain()
Query_2_condition = name_image

# work_table_1.perform_sql(Query_1_sql, Query_1_values)

date = work_table_1.get_data(Query_2_sql, Query_2_condition)

print(date)

work_table_1.close_DB()

if date:
    print(1)
else:
    print(0)
