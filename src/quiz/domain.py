from dataclasses import dataclass, field


class NoQuestionsException(Exception):
    pass


class NoMoreQuestionsException(Exception):
    pass


@dataclass
class Quiz:
    ix: str
    questions: list[str]


@dataclass
class Submission:
    quiz: Quiz
    ix: str = None
    responses: list[str] = field(default_factory=list)

    def __post_init__(self):
        if self.responses:
            return

        self.responses = ["" for _ in self.quiz.questions]

    def add_response(self, text) -> int:
        for ix, response in enumerate(self.responses):
            if response:
                continue
            self.responses[ix] = text
            return ix + 1
        else:
            raise NoMoreQuestionsException()
