# _*_ coding:utf8 _*_
from paper import db
from .companies import Companies


class Papers(db.Model):
    __tablename__ = 'papers'

    paper_id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.company_id'))
    paper_name = db.Column(db.String(255))

    @staticmethod
    def get_paper(paper_id):
        return Papers.query.filter_by(paper_id=paper_id).first()

    @staticmethod
    def get_id(paper_name):
        return Papers.query.filter_by(paper_name=paper_name).first().paper_id

    @staticmethod
    def add_paper(company_name, paper_name):
        if not Papers.query.filter_by(paper_name=paper_name).count():
            company_id = Companies.get_id(company_name)
            paper = Papers(company_id=company_id, paper_name=paper_name)
            db.session.add(paper)
            db.session.flush()
            paper_id = paper.paper_id
            db.session.commit()
            return paper_id

    @staticmethod
    def existed(paper_name):
        return True if Papers.query.filter_by(paper_name=paper_name).count() else False

    @staticmethod
    def get_all_paper():
        return Papers.query.all()

    @staticmethod
    def get_count():
        return db.session.query(Papers).count()



