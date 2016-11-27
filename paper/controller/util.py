# -*- coding:utf8 -*-
import os
import json
from ..model.companies import Companies
from ..model.papers import Papers
from ..model.questions import Questions
from ..model.options import Options
import re


QUESTION_TYPE = {
    '单选': 1,
    '多选': 2,
    '不定项选择': 3,
    '填空': 4,
    '判断': 5,
    '问答': 6,
    '简单': 7,
    '在线编程': 8
}


def row_convert(rows):
    if not rows:
        return {}

    if type(rows) == list:
        data = []
        for row in rows:
            data.append({c.name: str(getattr(row, c.name)) for c in row.__table__.columns})
        return data
    else:
        return {c.name: str(getattr(rows, c.name)) for c in rows.__table__.columns}


def add_paper(paper_content):
    paper = json.loads(paper_content)

    company_name = paper['company']
    paper_name = paper['name']

    if Papers.existed(paper_name=paper_name):
        return

    # 添加公司
    Companies.add_company(company_name=company_name)
    # 添加试卷
    paper_id = Papers.add_paper(company_name=company_name, paper_name=paper_name)

    # 添加问题
    for question in paper['content']:
        if question['type'] == '单选' or question['type'] == '多选' or question['type'] == '不定项选择':
            question_id = Questions.add_question(paper_id=paper_id,
                                                 content=question['name'],
                                                 answer=question['answer'],
                                                 ques_type=QUESTION_TYPE[question['type'].encode('utf-8')])
            # 添加选择题的选项
            for option in question['options']:
                Options.add_option(option_name=option['option_name'],
                                   content=option['content'],
                                   question_id=question_id)


def valid_email(email):
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email):
        return True
    return False


