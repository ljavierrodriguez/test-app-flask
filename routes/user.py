from flask import Blueprint, render_template, jsonify, request
from main import db
from models.user import User
from models.address import Address

routes_users = Blueprint('routes_users', __name__)

@routes_users.route("/users", methods=['GET', 'POST'])
@routes_users.route("/users/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def users(id = None):
    if request.method == 'GET':
        if id is not None:
            user = User.query.get(id)
            if user:
                return jsonify(user.serialize()), 200
            else:
                return jsonify({"msg": "User not found"}), 200
        else:
            users = User.query.all()
            users = list(map(lambda user: user.serialize(), users))
            return jsonify(users), 200
        
    if request.method == 'POST':
        username = request.json.get('username', None)
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        addresses = request.json.get('addresses', None)


        user = User()
        user.username = username
        user.email = email 
        user.password = password

        db.session.add(user)
        db.session.commit()
        
        if addresses:
            if len(addresses) > 1:
                for x in range(len(addresses)):
                    addrr = Address()
                    addrr.address = addresses[x]["address"]
                    addrr.user_id = user.id
                    db.session.add(addrr)
            else:
                addrr = Address()
                addrr.address = addresses[0]["address"]
                addrr.user_id = user.id
                db.session.add(addrr)
            
            db.session.commit()

        return jsonify(user.serialize()), 200

    if request.method == 'PUT':
        username = request.json.get('username', None)
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        addresses = request.json.get('addresses', None)


        user = User.query.get(id)
        user.username = username
        user.email = email 
        user.password = password

        db.session.commit()
        
        if addresses:
            if len(addresses) > 0:
                for x in range(len(addresses)):
                    if addresses[x]["id"]:
                        addrr = Address.query.get(addresses[x]["id"])
                        addrr.address = addresses[x]["address"]
                        addrr.user_id = user.id
                    else:
                        addrr = Address()
                        addrr.address = addresses[x]["address"]
                        addrr.user_id = user.id
                        db.session.add(addrr)
            
            db.session.commit()

        return jsonify(user.serialize()), 200

    if request.method == 'DELETE':
        pass