import psycopg2

connect = psycopg2.connect(
    dbname="proba", host="localhost", user="postgres", password="d13031998", port="5432"
)

print(connect)