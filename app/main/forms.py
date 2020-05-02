from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    pitch_title = StringField('Pitch title', validators=[Required()])
    pitch_content = TextAreaField('Write your pitch')
    category = StringField('Pitch category')
    submit = SubmitField('Submit your pitch')

class UpdateForm(FlaskForm):
    bio = TextAreaField('Tell us something about you',validators=[Required()])
    submit = SubmitField('Update bio')