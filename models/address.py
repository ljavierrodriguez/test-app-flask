from main import db
from models.user import User

class Address(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship(User)
    
    def __repr__(self):
        return '<Address %r>' % self.address

    def serialize(self):
        return {
            'id': self.id,
            'address': self.address,
            #'user': self.user.serialize(),
        }