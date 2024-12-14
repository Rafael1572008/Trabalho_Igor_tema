from database import db

class Product(db.Model):
    __tablename__ = 'Product'
    id_product = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Integer, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id_category'), nullable=False)

    category = db.relationship('Category', back_populates='products')
    orders_products = db.relationship('Orders_Products', back_populates='product', lazy=True)

    def __repr__(self):
        return f'<Product {self.name}>'

    def to_json(self):
        return {
            'id_product': self.id_product,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock_quantity': self.stock_quantity,
            'category': self.category.to_json() if self.category else None
        }
