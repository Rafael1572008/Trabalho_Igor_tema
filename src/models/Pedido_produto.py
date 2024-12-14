from database import db

class Orders_Products(db.Model):
    __tablename__ = 'Orders_Products'
    id_orders_products = db.Column(db.Integer, primary_key=True, autoincrement=True)
    orders_id = db.Column(db.Integer, db.ForeignKey('Orders.id_orders'), nullable=False)
    products_id = db.Column(db.Integer, db.ForeignKey('Product.id_product'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_f = db.Column(db.Integer, nullable=False)

    order = db.relationship('Orders', back_populates='orders_products')
    product = db.relationship('Product', back_populates='orders_products')

    def __repr__(self):
        return f'<Orders_Products {self.id_orders_products}>'

    def to_json(self):
        return {
            'id_orders_products': self.id_orders_products,
            'orders_id': self.orders_id,
            'products_id': self.products_id,
            'quantity': self.quantity,
            'total_f': self.total_f,
            'order': self.order.to_json() if self.order else None,
            'product': self.product.to_json() if self.product else None
        }
