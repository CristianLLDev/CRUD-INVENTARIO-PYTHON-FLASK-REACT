from flask import Blueprint, request, jsonify
from .models import Product
from . import db

bp = Blueprint('main', __name__)

@bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@bp.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

@bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    
    product = Product.query.get_or_404(id)
    product.name = data['name']
    product.price = data['price']
    db.session.commit()
    return jsonify(product.to_dict())

@bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return '', 204
