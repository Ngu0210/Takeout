from models.Menu import Menu
from models.User import User
from main import db
from flask import Blueprint, request, jsonify, abort, g
from schemas.MenuSchema import menu_schema, menus_schema
from flask_jwt_extended import jwt_required
from services.auth_service import verify_user, verify_admin
from sqlalchemy.orm import joinedload

menu = Blueprint("menu", __name__, url_prefix="/menu")

@menu.route("/", methods=["GET"])
def menu_index():
    #Returns the menu
    menu = Menu.query.all()
    serialised_data = menus_schema.dump(menu)
    return(jsonify(serialised_data))

@menu.route("/", methods=["POST"])
@jwt_required
def menu_create(user=None):
    #Creates new dish in menu
    menu_fields = menu_schema.load(request.json)

    new_menu = Menu()
    new_menu.title = menu_fields["title"]
    new_menu.price = menu_fields["price"]
    new_menu.vegetarian = menu_fields["vegetarian"]

    user.menu.append(new_menu)

    db.session.commit()

    return jsonify(menu_schema.dump(new_menu))

@menu.route("/<int:id>", methods=["GET"])
def menu_show(id):
    #Returns specific dish
    menu = Menu.query.get(id)
    return jsonify(menu_schema.dump(menu))

@menu.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
@verify_admin
def menu_update(id):
    #Updates specific dish
    menu_fields = menu_schema.load(request.json)

    menu = Menu.query.filter_by(id=id)

    menu.update(menu_fields)
    db.session.commit()

    return jsonify(menu_schema.dump(menu[0]))

@menu.route("/<int:id>", methods=["DELETE"])
@jwt_required
@verify_admin
def menu_delete(id):
    #Deletes specific dish

    menu = Menu.query.filter_by(id=id, user_id=user.id).first()

    if not menu:
        return abort(400)

    db.session.delete(menu)
    db.session.commit()

    return jsonify(menu_schema.dump(menu))