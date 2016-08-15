from flask_wtf import Form
from wtforms import StringField, FileField
from wtforms.validators import EqualTo, Required, Length
from flask.ext.login import login_user, logout_user, current_user
from ..models import User, Profile


class ProfileForm(Form):
    location = StringField('Location', validators=[
                           Required(), Length(max=100)])
    job = StringField('Job', validators=[Required(), Length(max=30)])
    position = StringField('Position', validators=[Required(), Length(max=20)])
    filed = StringField('Brief Introduction', validators=[
                        Required(), Length(max=20)])
    photo = FileField('Avatar')
