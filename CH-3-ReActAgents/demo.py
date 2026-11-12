import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "SalesDB", "Sales.db")
conn = sqlite3.connect(db_path)

cursor = conn.cursor()


cursor.execute("""select * from orders""")
rows = cursor.fetchall()
for row in rows:
        print(row)

conn.close()