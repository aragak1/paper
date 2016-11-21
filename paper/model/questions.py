from paper import db


class Questions(db.Model):
    __tablename__ = 'questions'

    question_id = db.Column(db.Integer, primary_key=True)
    paper_id = db.Column(db.Integer, db.ForeignKey('papers.paper_id'))
    content = db.Column(db.Text)
    answer = db.Column(db.Text)
    ques_type = db.Column(db.Integer, default=1)

    @staticmethod
    def get_questions(paper_id):
        return Questions.query.filter_by(paper_id=paper_id).all()

    @staticmethod
    def existed(question_id):
        return True if Questions.query.filter_by(question_id=question_id).count() else False

    @staticmethod
    def add_question(paper_id, content, answer, ques_type):
        question = Questions(paper_id=paper_id, content=content, answer=answer, ques_type=ques_type)
        db.session.add(question)
        db.session.flush()
        question_id = question.question_id
        db.session.commit()
        return question_id

    @staticmethod
    def get_answer(question_id):
        return Questions.query.filter_by(question_id=question_id).first().answer

