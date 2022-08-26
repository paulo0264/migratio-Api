from datetime import datetime
from config import db
from .tabelas import AppLicitacoes
from flask import jsonify, request
import datetime
import jwt
from config import app

def get_all():
  addrs = AppLicitacoes.query.all()
  return jsonify([addr.to_json() for addr in addrs]), 200

def get_by_id(id):
  addr = AppLicitacoes.query.get(id)
  if addr is None:
    return {"error": "Not found"}, 404
  return jsonify(addr.to_json())

def insert():
  if request.is_json:
    body = request.get_json()
    addr = AppLicitacoes (
      orgao = body["orgao"],
      titulo = body["titulo"],
      estado = body["estado"],
      cidade = body["cidade"],
      objeto = body["objeto"],
      datas = body["datas"]
     

    )
    db.session.add(addr)
    db.session.commit()
    payload = {
      "id": addr.id,
      "exp": datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'])

    return jsonify(token.decode('UTF-8')), 201
  return {"error": "Request must be JSON"}, 415


def update(id):
  if request.is_json:
    body = request.get_json()
    addr = AppLicitacoes.query.get(id)
    if addr is None:
      return {"error": "Not found"}, 404
    if("orgao" in body):
      addr.orgao = body["orgao"]
    if("titulo" in body):
      addr.titulo = body["titulo"]
    if("estado" in body):
      addr.estado = body["estado"]
    if("cidade" in body):
      addr.cidade = body["cidade"]
    if("objeto" in body):
      addr.objeto = body["objeto"]
    if("datas" in body):
      addr.datas = body["datas"]
    if("data" in body):
      addr.data = body["data"]
  
    db.session.add(addr)
    db.session.commit()
    return "Atualizado com sucesso", 200
  return {"error": "Request must be JSON"}, 415

def soft_delete(id):
  addr = AppLicitacoes.query.get(id)
  if addr is None:
      return {"error": "Not found"}, 404
  addr.active = False   
  db.session.add(addr)
  db.session.commit()
  return "Deletado com sucesso", 200