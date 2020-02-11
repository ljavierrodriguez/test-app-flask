from flask import Blueprint, render_template, jsonify

routes_main = Blueprint('routes_main', __name__)

@routes_main.route("/", methods=['GET'])
def home():
    return render_template('index.html')