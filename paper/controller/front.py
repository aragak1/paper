from paper import app
from flask import session, render_template
from ..model.companies import Companies


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/companies/<int:company_id>')
def companies(company_id):
    company_pic = Companies.get_picture(company_id)
    company_name = Companies.get_company_name(company_id)
    return render_template('companies.html',
                           company_id=company_id,
                           company_pic=company_pic,
                           company_name=company_name)


@app.route('/papers/<int:paper_id>')
def paper(paper_id):
    return render_template('paper.html', paper_id=paper_id)
