from flask import Flask
from application.views.main import main_bp
from application.views.choosing import choosing_bp
from application.views.fight import fight_bp
from application.views.errors import errors_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    app.register_blueprint(choosing_bp)
    app.register_blueprint(fight_bp, url_prefix="/fight/")
    app.register_blueprint(errors_bp)
    return app
