from flask import render_template,redirect,url_for,abort,request
from . import main
from .. import db,photos
from .forms import PitchForm,UpdateForm
from ..models import Pitch,User
from flask_login import login_required,current_user

@main.route('/')
def index():

    title = 'Welcome to Pitch ideas'

    return render_template('index.html',title=title)

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        title = form.pitch_title.data
        pitch = form.pitch_content.data
        category = form.category.data

        new_pitch = Pitch(pitch_title=title,pitch_content=pitch,category=category,user=current_user)

        new_pitch.save_pitch()

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

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitch/<int:id>')
def pitch(id):
    pitch = Pitch.get_pitch(id)

    return render_template('pitch.html',pitch=pitch)

@main.route('/<uname>/pitches')
def user_pitches(uname):
    pitches = Pitch.get_user_pitches(uname)

    return render_template('pitches.html',pitches=pitches)