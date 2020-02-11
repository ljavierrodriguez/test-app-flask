from main import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    addresses = db.relationship('Address', backref='users')

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        addresses = []

        if self.addresses:
            addresses = list(map(lambda addr: addr.serialize(), self.addresses))

        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'addresses': addresses
            
        }
