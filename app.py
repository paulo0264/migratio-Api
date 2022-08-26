from config import app
from flask_cors import CORS
from routes import AppLicitacoes




cors = CORS(app)

if __name__ == '__main__':

  app.register_blueprint(AppLicitacoes.app)
  app.run(debug=True, host="0.0.0.0", port=8090)