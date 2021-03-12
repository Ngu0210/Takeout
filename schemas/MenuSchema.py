from main import ma
from models.Menu import Menu
from marshmallow.validate import Length
from schemas.UserSchema import UserSchema

class MenuSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Menu

    title = ma.String(required=True, validate=Length(max=20))
    price = ma.Integer(required=False)
    vegetarian = ma.Boolean(required=False)
    portion = ma.String(required=False)

    # user = ma.Nested(UserSchema)

menu_schema = MenuSchema()
menus_schema = MenuSchema(many=True)