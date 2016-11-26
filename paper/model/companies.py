# _*_ coding:utf8 _*_
from paper import db


class Companies(db.Model):
    __tablename__ = 'companies'

    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(255))
    introduction = db.Column(db.Text)
    picture = db.Column(db.String(255), default='/static/img/company.png')

    @staticmethod
    def get_all_companies():
        return Companies.query.all()

    @staticmethod
    def get_company(company_id):
        return Companies.query.filter_by(company_id=company_id).first()

    @staticmethod
    def get_company_name(company_id):
        return Companies.query.filter_by(company_id=company_id).first().company_name

    @staticmethod
    def add_company(company_name, introduction='introduction', picture='/static/img/company.png'):
        if not Companies.query.filter_by(company_name=company_name).count():
            company = Companies(company_name=company_name, introduction=introduction, picture=picture)
            db.session.add(company)
            db.session.commit()

    @staticmethod
    def del_company(company_name):
        companies = Companies.query.filter_by(company_name=company_name)
        if companies.count():
            company = companies.first()
            db.session.delete(company)
            db.session.commit()

    @staticmethod
    def existed(company_name):
        return True if Companies.query.filter_by(company_name=company_name).count() else False

    @staticmethod
    def get_id(company_name):
        return Companies.query.filter_by(company_name=company_name).first().company_id

    @staticmethod
    def get_count():
        return db.session.query(Companies).count()

    @staticmethod
    def get_picture(company_id):
        return Companies.query.filter_by(company_id=company_id).first().picture
