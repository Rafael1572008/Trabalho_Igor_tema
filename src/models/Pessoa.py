from database import db

class Person(db.Model):
    __tablename__ = 'Person'
    id_person = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    access_level = db.Column(db.String(90), nullable=False)
    telefone = db.Column(db.String(50), nullable=False)
    register_date = db.Column(db.String(50), nullable=False)

    orders = db.relationship('Orders', back_populates='person', lazy=True)

    def __repr__(self):
        return f'<Person {self.name}>'

    def to_json(self):
        return {
            'id_person': self.id_person,
            'name': self.name,
            'email': self.email,
            'telefone': self.telefone,
            'register_date': self.register_date
        }
