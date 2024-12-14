from database import db

class Category(db.Model):
    __tablename__ = 'Category'
    id_category = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    products = db.relationship('Product', back_populates='category', lazy=True)

    def __repr__(self):
        return f'<Category {self.name}>'

    def to_json(self):
        return {
            'id_category': self.id_category,
            'name': self.name,
            'description': self.description
        }
