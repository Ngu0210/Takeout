from main import db
from sqlalchemy.sql import func

class Order(db.Model):
    __tablename__ = "user_order"

    id = db.Column(db.Integer, db.Sequence('order_id_seq'), primary_key=True)
    date_time = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
    menu_id = db.Column(db.Integer, db.ForeignKey("menu.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    def __repr__(self):
        return f"<Order {self.id}, {self.date_time}>"

order = Order()