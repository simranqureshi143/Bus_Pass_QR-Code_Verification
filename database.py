import sqlite3

conn = sqlite3.connect("bus_pass.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS bus_pass (
    pass_id TEXT PRIMARY KEY,
    name TEXT,
    route TEXT,
    valid_to TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

print("✅ Database & table created")
