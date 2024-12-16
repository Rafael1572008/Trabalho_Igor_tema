from models import Pedido, db
from sqlalchemy.orm import joinedload

class PedidoDAO:

    @staticmethod
    def add_pedido(name, description):
        new_category = Category(name = name, description = description)
        db.session.add(new_category)
        db.session.commit()
        return new_category
    
    @staticmethod
    def get_pedido(id_category):
        return Category.query.get(id_category)