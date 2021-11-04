from dataclasses import dataclass
from typing import Protocol

from quiz.domain import Quiz, Submission, NoQuestionsException


class Resource(Protocol):
    def to_dict(self) -> dict:
        pass

    def get_one(cls) -> dict:
        pass

    def get_single(cls, ix: str) -> dict:
        pass

    def upsert(cls, **kwargs: dict) -> dict:
        pass


@dataclass
class GetQuizCase:
    resource: Resource

    def get_quiz(self) -> Quiz:
        quiz = self.resource.get_one()
        quiz = Quiz(**quiz)

        if not quiz.questions:
            raise NoQuestionsException()

        return quiz

    def get_step(self, ix: str, step: int = -1) -> Quiz:
        quiz = self.resource.get_single(ix)

        quiz = Quiz(**quiz)

        return quiz


@dataclass
class CreateSubmissionCase:
    quiz_resource: Resource
    submission_resource: Resource

    def create(self, quiz_ix: str, text: str) -> Submission:
        quiz = self.quiz_resource.get_single(quiz_ix)

        quiz = Quiz(**quiz)

        submission = self.submission_resource.upsert(quiz=quiz.ix)
        submission["quiz"] = quiz

        submission = Submission(**submission)

        submission.add_response(text)

        self.submission_resource.upsert(asdict(**submission))

        return submission

    def add_response(self, ix: str, text: str) -> int:
        submission = self.submission_resource.get_single(ix)

        submission = Submission(**submission)

        response = submission.add_response(text)

        self.submission_resource.upsert(asdict(**submission))

        return response
