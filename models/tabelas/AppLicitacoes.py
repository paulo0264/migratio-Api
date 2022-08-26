from config import db

class AppLicitacoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orgao = db.Column(db.String(50))
    titulo = db.Column(db.Integer)
    estado = db.Column(db.String(50))
    cidade = db.Column(db.String(50))
    objeto = db.Column(db.String(50))
    datas = db.Column(db.Date)
    data = db.Column(db.DateTime, server_default=db.func.now())

    def to_json(self):
       return {
        "id": self.id,
        "orgao": self.orgao,
        "titulo": self.titulo,
        "estado": self.estado,
        "cidade": self.cidade,
        "objeto": self.objeto,
        "datas": self.datas,
        "data": self.data
       
    }