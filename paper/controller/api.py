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


@app.route('/api/papers/companies/<int:company_id>')
def get_company_papers(company_id):
    return jsonify({'items': row_convert(Papers.get_company_papers(company_id))})


@app.route('/api/papers/<int:paper_id>')
def get_paper(paper_id):
    d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}
    data = {}

    paper = row_convert(Papers.get_paper(paper_id=paper_id))
    data['paper_name'] = paper['paper_name']
    data['company_name'] = Companies.get_company_name(paper['company_id'])

    questions = row_convert(Questions.get_questions(paper_id=paper_id))
    questions = [q for q in questions if q['ques_type'] == '1']
    for question in questions:
        question['options'] = row_convert(Options.get_options(question_id=question['question_id']))

    # 修改成前端所需的数据格式
    for question in questions:
        question.update(question=question.pop('content'))
        question.update(correctAnswer=d[question.pop('answer')])
        question['answers'] = []
        for option in question['options']:
            question['answers'].append(option['content'])
        question.pop('options')

    return jsonify({'questions': questions})


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
