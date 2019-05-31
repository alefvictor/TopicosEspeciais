import sqlite3

conn = sqlite3.connect('shallow.db')

cursor = conn.cursor()

cursor.execute("""
    SELECT *
    FROM tb_estudante;
""")

for linha in cursor.fetchall():
    print("Bom dia, ", linha[1])

conn.close()
