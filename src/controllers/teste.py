from flask import Flask, Blueprint
from DAO import CategoryDAO

teste = Blueprint('teste', __name__)

@teste.route('/add')
def add():

    name = "Colar"
    description = "Bolas Brilhantes"

    category = CategoryDAO.add_category(name = name, description = description)

    print(f"categoria adicionado: {category.to_json()}")
    return "Categoria adicionada com sucesso!"



