from models import Category, db
from sqlalchemy.orm import joinedload

class CategoryDAO:

    @staticmethod
    def add_category(name, description):
        new_category = Category(name = name, description = description)
        db.session.add(new_category)
        db.session.commit()
        return new_category
    
    @staticmethod
    def get_category(id_category):
        return Category.query.all(id_category)