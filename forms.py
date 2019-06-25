from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class AddItem(FlaskForm):
    title = StringField('Title',
                           validators=[DataRequired(), Length(min=2, max=100)])
    description = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')
