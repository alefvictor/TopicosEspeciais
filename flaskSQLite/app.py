from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ("Olá Mundo! Estou aprendendo Flask", 200)

@app.route("/alunos", methods=['GET'])
def getAlunos():
    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT *
    FROM tb_aluno;
    """)
    for linha in cursor.fetchall():
        print(linha)
    conn.close()
    return("executado", 200)

@app.route("/alunos<int:id>", methods=['GET'])
def getAlunosByID():
    pass

@app.route("/aluno", methods=['POST'])
def setAluno():
    print ('Cadastrando o aluno')
    Nome = request.form["Nome"]
    Nascimento = request.form["Nascimento"]
    Matricula = request.form["Matricula"]
    Cpf = request.form["Cpf"]
    return ('Cadastrado com sucesso', 200)
    Conn = sqlite3.connect("escola2.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO tb_aluno(Nome, Matricula, Cpf, Nascimento)
    VALUES(?, ?, ?, ?);
    """, (Nome, Matricula, Cpf, Nascimento))
    Conn.commit()
    conn.close()

@app.route("/cursos", methods=['GET'])
def getCursos():
    pass

@app.route("/cursos<int:id>", methods=['GET'])
def getCursosByID():
    pass

@app.route("/turmas", methods=['GET'])
def getTurmas():
    pass

@app.route("/turmas<int:id>", methods=['GET'])
def getTurmasByID(id):
    pass


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
