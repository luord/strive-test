from dataclasses import dataclass, asdict
from uuid import uuid4

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


@dataclass
class Quiz(db.Model):  # type: ignore
    ix: str = db.Column(
        db.String(36), primary_key=True, default=lambda: str(uuid4())
    )
    questions: list[str] = db.Column(db.JSON)

    def to_dict(self):
        data = asdict(self)

        return data


@dataclass
class Submission(db.Model):  # type: ignore
    ix: str = db.Column(
        db.String(36), primary_key=True, default=lambda: str(uuid4())
    )
    quiz: str = db.Column(db.String, db.ForeignKey("quiz.ix"), nullable=False)
    responses: list[str] = db.Column(db.JSON)

    def to_dict(self):
        data = asdict(self)

        return data
