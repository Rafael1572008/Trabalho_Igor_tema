from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Orders(db.Model):
    __tablename__ = 'Orders'
    id_orders = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('Person.id_person'), nullable = False)
    date = db.Column(db.String(40), nullable = False)
    status = db.Column(db.String(50), nullable = False)
    tatal = db.Column(db.Integer, nullable = False)

    order = db.relationship('order', back_populates='persons', lazy=True)  # relacao com person
    order_producst_2 = db.relationship('order_producst_2', back_populates = 'order_producst', lazy=True)

class Person(db.Model):
    __tablename__ = 'Person'
    id_person = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(50), nullable = False)
    access_level = db.Column(db.String(90), nullable = False)
    telefone = db.Column(db.String(50), nullable = False)
    register_date = db.Column(db.String(50), nullable = False)

    persons = db.relationship('persons', back_populates='order', lazy=True) # Relacao com orders
    
class Category(db.Model):
    __tablename__ = 'Category'
    id_category = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text)

    categorys = db.relationship('categorys', back_populates='products', lazy=True) # Relacao com produto

class Product(db.Model):
    __tablename__ = 'Product'
    id_product = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text)
    price = db.Column(db.Integer, nullable = False)
    stock_quantity = db.Column(db.Integer, nullable = False)
    category_id = db.Column(db.Integer, nullable = False)

    products = db.relationship('products', back_populates = 'categorys')
    order_producst_1 = db.relationship('order_producst_1', back_populates = 'order_producst', lazy=True)
    

class Orders_Products(db.Model):
    __tablename__ = 'Orders_Products'
    id_orders_products = db.Column(db.Integer, primary_key=True)
    orders_id = db.Column(db.Integer, db.ForeignKey('Orders.id_orders'), nullable = False)
    products_id = db.Column(db.Integer, db.ForeignKey('Product.id_product'), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    total_f = db.Column(db.Integer, nullable = False)

    order_producst = db.relationship('order_producst', back_populates = 'order_producst_1', lazy=True)
    order_producst_3 = db.relationship('order_producst_2', back_populates = 'order_producst_2', lazy=True)

    if __name__ == "__main__":
        with app.app_context():
            db.create_all()
        app.run()

categoria = Category(id_category = 1, name = "Colar", description = "Coala")
db.session.add(categoria)
db.session.commit()

try:
    db.session.commit()
except Exception as e:
    db.session.rollback()
    print (f"ERRO:  {e}")    


