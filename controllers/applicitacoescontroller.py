from models import applicitacoesModel
from flask import requests

def get_all():
    request = requests.get("http://nadic.ifrn.edu.br/api/dou/2022-02-08/?usuario=dev_nadic")
    todos = json.loads(request.content)
    print(todos)
    return applicitacoesModel.get_all()

def get_by_id(id):
  return applicitacoesModel.get_by_id(id)

def insert():
  return applicitacoesModel.insert()

def update(id):
  return applicitacoesModel.update(id)

def delete(id):
  return applicitacoesModel.soft_delete(id)