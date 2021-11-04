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

    def to_dict(self) -> dict:
        data = asdict(self)

        return data

    @classmethod
    def get_one(cls) -> dict:
        return cls.query.first().to_dict()

    @classmethod
    def get_single(cls, ix: str) -> dict:
        return cls.query.get(ix).to_dict()

    @classmethod
    def upsert(cls, **kwargs: dict) -> dict:
        instance = cls(**kwargs)
        db.session.add(instance)

        db.session.commit()
        return instance.to_dict()


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

    @classmethod
    def get_one(cls) -> dict:
        return cls.query.first().to_dict()

    @classmethod
    def get_single(cls, ix: str) -> dict:
        return cls.query.get(ix).to_dict()

    @classmethod
    def upsert(cls, **kwargs: dict) -> dict:
        instance = cls(**kwargs)
        db.session.add(instance)

        db.session.commit()
        return instance.to_dict()
