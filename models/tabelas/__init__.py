from .AppLicitacoes import AppLicitacoes
from config import db

__all__ = [
 
  'AppLicitacoes'
]

db.create_all()