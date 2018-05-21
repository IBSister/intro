import psycopg2

conn = psycopg2.connect(database = "test1", user = "postgres", password = "IBSisters", host = "127.0.0.1", port = "5432")

cur = conn.cursor()

cur.execute("INSERT INTO TEAM (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'CHRIS', 16, 'AZ', 200)");

conn.commit()
print("Records created successfully")
conn.close()