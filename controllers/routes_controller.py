from flask import Blueprint, abort, jsonify, request, render_template, url_for, flash, redirect, request

routes = Blueprint("routes", __name__)

@routes.route('/')
@routes.route('/home')
def home():
    return render_template('index.html', title='Home')

