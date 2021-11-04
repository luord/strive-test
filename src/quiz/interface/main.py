from dataclasses import asdict

from flask import Blueprint, render_template, redirect, request, session, url_for
from flask.views import MethodView

from quiz.repository import Quiz, Submission
from quiz.cases import GetQuizCase, CreateSubmissionCase


bp = Blueprint("interface", __name__)


class Root(MethodView):
    def get(self):
        quiz_case = GetQuizCase(Quiz)

        quiz = quiz_case.get_quiz()
        session["quiz"] = quiz.ix
        return render_template("question.j2", quiz=asdict(quiz), step=0)

    def post(self):
        submission_case = CreateSubmissionCase(Quiz, Submission)

        submission = submission_case.create(session["quiz"], request.form["response"])
        session["submission"] = submission.ix

        return redirect(url_for('interface.step', step=1))


class Step(MethodView):
    def get(self, step):
        quiz_case = GetQuizCase(Quiz)

        quiz = quiz_case.get_step(session["quiz"], step)

        return render_template("question.j2", quiz=asdict(quiz), step=step)

    def post(self, step):
        submission_case = CreateSubmissionCase(Quiz, Submission)

        try:
            step = submission_case.add_response(session["submission"], request.form["response"])
        except:
            return "All done, thanks!"

        return redirect(url_for('interface.step', step=step))


bp.add_url_rule("/", view_func=Root.as_view("root"))
bp.add_url_rule("/<int:step>", view_func=Step.as_view("step"))
