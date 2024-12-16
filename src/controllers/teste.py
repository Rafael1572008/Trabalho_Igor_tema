from flask import Blueprint
from repository import CategoriaRepository

teste = Blueprint('teste', __name__)

@teste.route('/filter')
def add():
    id = 1
    name = "Batom"
    description = "batom vrilahnte"

    repository = CategoriaRepository()
    category = repository.edit_category(id_category = id, name=name, description = description)

    print(f"Categoria alterado: {category}")
    return f"Categoria alterado com sucesso!"
