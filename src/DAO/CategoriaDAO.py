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
        return Category.query.get(id_category)

    @staticmethod
    def get_all_category():
        return Category.query.all()

    @staticmethod
    def get_filter_category(name):
        query = Category.query.filter((Category.name.ilike(f"%{name}%")))
        return query.all()

    @staticmethod
    def edit_category(id_category, name, description):
        category = CategoryDAO.get_category(id_category)
        if name:
            category.name = name
            db.session.commit()
        return category    