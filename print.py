import psycopg2

conn = psycopg2.connect(database = "test1", user = "postgres", password = "IBSisters", host = "127.0.0.1", port = "5432")

cur = conn.cursor()

cur.execute("SELECT id, name, address, salary from TEAM")
rows = cur.fetchall()
for row in rows:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n" )
id1 = row[0]
cur.execute("")
print("Operation Successful")
conn.close()