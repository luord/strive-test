from os import getcwd, getenv
from pathlib import Path

from flask import Flask

from quiz.interface.main import bp
from quiz.interface.admin import admin

from quiz.repository import db


INIT_PARAMS = {
    "root_path": getcwd(),
    "template_folder": str(Path("src", "templates")),
}


def create_app(init_params=INIT_PARAMS):
    app = Flask(__name__, **init_params)
    app.config["SECRET_KEY"] = getenv("FLASK_SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"

    app.register_blueprint(bp)

    admin.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
