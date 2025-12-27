import sqlite3
from datetime import date

def verify(pass_id):
    conn = sqlite3.connect("bus_pass.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT valid_to, status FROM bus_pass WHERE pass_id=?",
        (pass_id,)
    )

    row = cur.fetchone()
    conn.close()

    if row:
        valid_to, status = row
        today = str(date.today())

        if status == "ACTIVE" and valid_to >= today:
            return "✅ VALID PASS"
        else:
            return "❌ EXPIRED PASS"
    else:
        return "❌ INVALID PASS"

