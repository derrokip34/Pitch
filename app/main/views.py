from flask import render_template,redirect,url_for
from . import main
from .. import db
from .forms import PitchForm
from ..models import Pitch

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/pitch/new', methods = ['GET','POST'])
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        pitch = Pitch(pitch_title = form.pitch_title.data, pitch_content = form.pitch_content.data,category = form.category.data)
        db.session.add(pitch)
        db.session.commit()

        return redirect(url_for('.index'))

    return render_template('new_pitch.html', form = form)