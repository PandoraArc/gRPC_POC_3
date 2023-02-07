import os
from flask import Flask 

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = "test"
    )
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route("/", methods=['GET'])
    def home():
        return "Hello! wrold"
    
    @app.route("/ping", methods=['GET'])
    def ping():
        return "200OK"
    
    from . import grpc_app
    app.register_blueprint(grpc_app.bp)
    
    return app