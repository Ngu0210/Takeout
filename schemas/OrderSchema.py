from main import ma
from models.Order import Order

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order

    date_time = ma.String(required=True)
    test = ma.String()

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)