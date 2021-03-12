from flask import Blueprint, jsonify
from models.Order import Order
from schemas.OrderSchema import order_schema, orders_schema

order = Blueprint("order", __name__, url_prefix="/order")

@order.route("/", methods=["GET"])
def order_index():
    order = Order.query.all()
    serialized_data = order_schema.dump(order)
    return jsonify(serialized_data)

@order.route("/", methods=["POST"])
def order_menu():
    order_field = order_schema.load(request.json)

