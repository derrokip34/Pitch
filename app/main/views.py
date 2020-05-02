from flask import render_template,redirect,url_for,abort
from . import main
from .. import db
from .forms import PitchForm,UpdateForm
from ..models import Pitch,User
from flask_login import login_required

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        pitch = Pitch(pitch_title = form.pitch_title.data, pitch_content = form.pitch_content.data,category = form.category.data)
        db.session.add(pitch)
        db.session.commit()

        return redirect(url_for('.index'))

    return render_template('new_pitch.html', form = form)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html',user=user)

@main.route('/user/<uname>/update', methods=["GET","POST"])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    update = UpdateForm()

    if update.validate_on_submit():
        user.bio = update.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname = user.username))

    return render_template('profile/update.html',update=update)