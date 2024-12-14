from flask import Blueprint
from repository import CategoriaRepository

teste = Blueprint('teste', __name__)

@teste.route('/add')
def add():
    name = "Brincos"
    description = "Bolas Brilhantes nas orelhas"

    repository = CategoriaRepository()
    category = repository.add_category(name=name, description=description)

    print(f"Categoria adicionada: {category}")
    return "Categoria adicionada com sucesso!"
