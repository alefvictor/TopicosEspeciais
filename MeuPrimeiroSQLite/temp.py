import sqlite3

conn = sqlite3.connect('shallow.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE tb_estudante(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(30) NOT NULL,
    endereco TEXT NOT NULL,
    nascimento DATE NOT NULL,
    matricula VARCHAR(12) NOT NULL
    );
""")
print('Tabela criada com sucesso.')
conn.close()
