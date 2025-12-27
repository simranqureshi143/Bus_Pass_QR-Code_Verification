import sqlite3

conn = sqlite3.connect("bus_pass.db")
cur = conn.cursor()

cur.execute("""
INSERT OR REPLACE INTO bus_pass VALUES
('PASS001', 'Simran', 'Route-21', '2025-12-31', 'ACTIVE')
""")

conn.commit()
conn.close()

print("✅ Bus pass inserted")
