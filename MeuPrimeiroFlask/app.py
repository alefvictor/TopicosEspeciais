from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/noticias/<categoria>")
def getNoticias(categoria):
    pass
@app.route("/usuario/<int:id>", methods=['GET'])
def getUsuario(id):
    usuarios = [{1: "joão"}, {2: "Maria"}, {3: "José"}]
    for usuario in usuarios:
        if (id in usuario.keys()):
            print(usuario[id])
            return (usuario[id], 200)

if(__name__== '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
