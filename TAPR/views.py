from flask_admin.contrib.sqla import ModelView
import flask_login as login 
from TAPR.models import User
class AdminView(ModelView): 
    def is_accessible(self):
        if login.current_user.is_authenticated: 
            if login.current_user.get_id():
                user = User.query.get(login.current_user.get_id())
                return not user.is_student
            return False