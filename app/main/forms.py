from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,SelectField,PasswordField
from wtforms.validators import Required,Email,EqualTo

class PitchForm(FlaskForm):
    pitch_title = StringField('Pitch title', validators=[Required()])
    pitch_content = TextAreaField('Write your pitch')
    category = SelectField('Pitch category', choices=[('interview','Interview pitch'),('product','Product pitch'),('promotion','Promotion pitch'),('movie','Movie-idea'),('educational','Educational pitch')],validators=[Required()])
    submit = SubmitField('Submit your pitch')

class UpdateForm(FlaskForm):
    bio = TextAreaField('Tell us something about you',validators=[Required()])
    submit = SubmitField('Update bio')

class CommentForm(FlaskForm):
    comments = TextAreaField('Leave a comment below',validators=[Required()])
    submit = SubmitField('Submit your comment')

class RequestForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    submit = SubmitField('Request password reset')

class ResetForm(FlaskForm):
    password = PasswordField('Password', validators=[Required()])
    confirm_password = PasswordField('Confirm Password',validators=[Required(),EqualTo('password')])
    submit = SubmitField('Reset Password')