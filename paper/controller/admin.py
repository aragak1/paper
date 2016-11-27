from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from ..model.users import Users
from ..model.companies import Companies
from ..model.papers import Papers
from ..model.questions import Questions
from ..model.options import Options
from paper import admin, db
import os.path as op


admin.add_view(ModelView(Users, db.session))
admin.add_view(ModelView(Companies, db.session))
admin.add_view(ModelView(Papers, db.session))
admin.add_view(ModelView(Questions, db.session))
admin.add_view(ModelView(Options, db.session))

img_path = op.join(op.dirname(__file__)[0: -10], 'static/img')
admin.add_view(FileAdmin(img_path, '/static/img', name='Image'))
