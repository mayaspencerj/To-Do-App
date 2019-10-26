from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

#FORM TO CREATE TO DO ITEMS

class CreateForm(FlaskForm):
    title = StringField('Title',
                           validators=[DataRequired(), Length(min=2, max=20)])
    content = StringField('Content', validators=[DataRequired(), Length(min=2, max=80)])
    submit = SubmitField('Create Item')
