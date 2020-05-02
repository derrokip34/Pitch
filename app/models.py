from . import db

class Pitch(db.Model):
    
    __tablename__ ='posts'
    id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String(255))
    pitch_content = db.Column(db.String(255))
    category = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.title}'