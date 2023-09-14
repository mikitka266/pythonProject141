from flask_wtf import FLaskForm
from wtforms import StringField, PasswordField, SelectField
from wtfforms.validators import DataRequired, Email, Length. EqualTo




class RegistrationForm(FLaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])


