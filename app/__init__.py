from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    CORS(app)  # Permite todas las solicitudes CORS
       
    db.init_app(app)
    
    with app.app_context():
        # Importar modelos y crear las tablas en la base de datos
        from . import models
        db.create_all()
    
    # Registrar rutas
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app
