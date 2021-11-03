from flask import Blueprint, render_template
from flask.views import View


bp = Blueprint("interface", __name__)


class Root(View):
    def dispatch_request(self):
        return render_template("root.j2")


bp.add_url_rule("/", view_func=Root.as_view("root"))
