from flask import Flask
from database import init_db
from controllers import teste

app = Flask(__name__)

app.register_blueprint(teste)

@app.route('/')
def index():
    return '<p>Hello, Word</p>'

if __name__ == "__main__":
    with app.app_context():
        # Inicializar o banco de dados
        init_db(app)

        # Criar tabelas no banco de dados
        app.run(debug=True)