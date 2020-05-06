from flask import render_template,redirect,url_for,abort,request
from . import main
from .. import db,photos
from .forms import PitchForm,UpdateForm,CommentForm,RequestForm,ResetForm
from ..models import Pitch,User,Comments
from flask_login import login_required,current_user

@main.route('/')
def index():

    pitches = Pitch.query.all()

    title = 'Welcome to Pitch ideas'

    return render_template('index.html',title=title,pitches=pitches)

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        title = form.pitch_title.data
        pitch = form.pitch_content.data
        category = form.category.data

        new_pitch = Pitch(pitch_title=title,pitch_content=pitch,category=category,user=current_user,likes=0,dislike=0)

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

@main.route('/pitch/<int:id>',methods=["GET","POST"])
def pitch(id):
    pitch = Pitch.get_pitch(id)
    
   

    if request.args.get("like"):
        pitch.likes = pitch.likes + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect(url_for('.pitch',id=pitch.id))

    elif request.args.get("dislike"):
        pitch.dislikes = pitch.dislikes + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect(url_for('.pitch',id=pitch.id))

    comments = Comments.get_comments(pitch)

    return render_template('pitch.html',pitch=pitch,comments=comments)

@main.route('/<uname>/pitches')
def user_pitches(uname):
    pitches = Pitch.get_user_pitches(uname)

    return render_template('pitches.html',pitches=pitches)

@main.route('/pitch/<int:id>/comment',methods=["GET","POST"])
@login_required
def comment(id):
    pitch = Pitch.get_pitch(id)
    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        comment=comment_form.comments.data

        new_comment = Comments(comment=comment,review=pitch,user=current_user)
        new_comment.save_comment()

        return redirect(url_for('.pitch',id=pitch.id))

    return render_template('comment.html',comment_form=comment_form)