from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


#FORM TO CREATE TO DO ITEMS
#THIS IS CALLED ON IN APP.PY 
class CreateForm(FlaskForm):
    title = StringField('Title',
                           validators=[DataRequired(), Length(min=2, max=50)])
    content = StringField('Content', validators=[DataRequired(), Length(min=2, max=10000)])
    submit = SubmitField('Create Item')
