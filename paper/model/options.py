# _*_ coding:utf8 _*_
from paper import db
from .questions import Questions


class Options(db.Model):
    __tablename__ = 'options'

    option_id = db.Column(db.Integer, primary_key=True)
    option_name = db.Column(db.String(16))
    content = db.Column(db.Text)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'))

    @staticmethod
    def add_option(option_name, content, question_id):
        if Questions.existed(question_id):
            option = Options(option_name=option_name, content=content, question_id=question_id)
            db.session.add(option)
            db.session.commit()

    @staticmethod
    def get_options(question_id):
        return Options.query.filter_by(question_id=question_id).all()
