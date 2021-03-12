from models.User import User
from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import abort, g

def verify_user(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()

        user = User.query.get(user_id)

        if not user:
            return abort(401, description="Invalid user")

        g.user = user

        return function(*args, user=user, **kwargs)
        
    return wrapper

def verify_admin(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()

        user = User.query.get(user_id)

        if not user:
            return abort(401, description="Invalid user")

        if user.admin == False:
            return abort(401, description="Invalid Privileges")

        g.user = user 

        return function(*args, user=user, **kwargs)
        
    return wrapper