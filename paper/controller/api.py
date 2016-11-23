# -*- coding: utf8 -*-
from paper import app
from paper.model.companies import Companies
from paper.model.papers import Papers
from paper.model.questions import Questions
from paper.model.options import Options
from util import row_convert, add_papers
from flask import jsonify


@app.route('/api/companies')
def get_all_companies():
    return jsonify({'companies': row_convert(Companies.get_all_companies()),
                    'count': Companies.get_count()})


@app.route('/api/companies/<int:company_id>')
def get_company(company_id):
    return jsonify(row_convert(Companies.get_company(company_id)))


@app.route('/api/papers/<int:paper_id>')
def get_paper(paper_id):
    data = {}

    paper = row_convert(Papers.get_paper(paper_id=paper_id))
    data['paper_name'] = paper['paper_name']
    data['company_name'] = Companies.get_company_name(paper['company_id'])

    questions = row_convert(Questions.get_questions(paper_id=paper_id))
    for question in questions:
        question['options'] = row_convert(Options.get_options(question_id=question['question_id']))

    return jsonify(questions)


@app.route('/api/answer/<int:question_id>')
def get_answer(question_id):
    return jsonify(Questions.get_answer(question_id=question_id))


@app.route('/api/papers')
def get_all_papers():
    return jsonify({'papers': row_convert(Papers.get_all_paper()),
                    'count': Papers.get_count()})


@app.route('/test')
def test():
    # add_papers('../papers')
    return 'done'
