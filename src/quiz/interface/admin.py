from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from quiz.repository import db, Quiz


admin = Admin()
admin.add_view(ModelView(Quiz, db.session))
