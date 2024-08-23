from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    jwt.init_app(app)
    Migrate(app, db)

    try:
        # Register blueprints after initialization
        from app.routes.auth_route import auth_blueprint as auth
        from app.routes.note_route import note_blueprint as note

        # Register blueprints with a URL prefix
        app.register_blueprint(auth, url_prefix='/auth')
        app.register_blueprint(note, url_prefix='/note')

        print("Routes blueprint registered successfully.")
    except ImportError as e:
        print(f"Error importing routes: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Default welcome endpoint
    @app.route('/')
    def welcome():
        return {"message": "Welcome to the Markdown Note-taking API built with Python-Django!"}, 200
    
    # Custom 404 error handler
    @app.errorhandler(404)
    def not_found(error):
        return {"error": "The requested URL was not found on the server. If you entered the URL manually, please check your spelling and try again."}, 404

    return app
