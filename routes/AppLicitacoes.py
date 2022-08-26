from flask import Blueprint
from controllers import applicitacoescontroller

app=Blueprint('applicitacoes', __name__)

@app.route("/applicitacoes", methods=["GET"])
def get_usuarios():
  return applicitacoescontroller.get_all()

@app.route("/applicitacoes/<int:id>", methods=["GET"])
def get_usuarios_by_id(id):
  return applicitacoescontroller.get_by_id(id)

@app.route("/applicitacoes", methods=["POST"])
def insert_addr():
  return applicitacoescontroller.insert()

@app.route("/applicitacoes/<int:id>", methods=["PUT"])
def update_addr(id):
  return applicitacoescontroller.update(id)

@app.route("/applicitacoes/<int:id>", methods=["DELETE"])
def delete_usuarios(id):
  return applicitacoescontroller.delete(id) 