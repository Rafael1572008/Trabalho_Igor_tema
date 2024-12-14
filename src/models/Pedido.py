from database import db

class Orders(db.Model):
    __tablename__ = 'Orders'
    id_orders = db.Column(db.Integer, primary_key=True, autoincrement=True)
    person_id = db.Column(db.Integer, db.ForeignKey('Person.id_person'), nullable=False)
    date = db.Column(db.String(40), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    total = db.Column(db.Integer, nullable=False)

    person = db.relationship('Person', back_populates='orders')
    orders_products = db.relationship('Orders_Products', back_populates='order', lazy=True)

    def __repr__(self):
        return f'<Orders: {self.id_orders}>'

    def to_json(self):
        return {
            'id_orders': self.id_orders,
            'person_id': self.person_id,
            'date': self.date,
            'status': self.status,
            'total': self.total,
            'person': self.person.to_json() if self.person else None
        }
