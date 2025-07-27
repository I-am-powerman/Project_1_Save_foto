from driver_sql import driver_sql

first_insert = driver_sql("proba", "postgres")

vaslues_1_insert = ["sjnvjinrv"]
first_insert.insert_sql("table_1", "name_1", vaslues_1_insert)
first_insert.close_DB()