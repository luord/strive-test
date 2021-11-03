from os import getcwd, getenv
from pathlib import Path

from flask import Flask

from quiz.interface import bp


INIT_PARAMS = {
    "root_path": getcwd(),
    "template_folder": str(Path("src", "templates")),
}


def create_app(init_params=INIT_PARAMS):
    app = Flask(__name__, **init_params)
    app.config["SECRET_KEY"] = getenv("FLASK_SECRET_KEY")

    app.register_blueprint(bp)

    return app
