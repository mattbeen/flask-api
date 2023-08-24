from flask import Blueprint, Flask, jsonify, request
from transform import create_stock_bp
from config import api_prefix

def create_app():
    app = Flask(__name__)
    stock_bp = create_stock_bp()
    app.register_blueprint(stock_bp,url_prefix = api_prefix)
    return app