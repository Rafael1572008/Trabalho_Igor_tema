from DAO import CategoryDAO

class CategoriaRepository:
    def __init__(self) -> None:
        self.category_dao = CategoryDAO()

    def get_category(self, id_category):
        return self.category_dao.get_category(id_category)
    
    def add_category(self, name, description):
        return self.category_dao.add_category(name, description)
