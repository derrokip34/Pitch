import unittest
from app.models import Pitch,User
from flask_login import current_user
from app import db

class TestPosts(unittest.TestCase):

    def setUp(self):
        self.user_Derrick = User(username="derrokip34",password="zlatan",email="derrokip@gmail.com")
        self.new_pitch = Pitch(pitch_title="Batwoman",pitch_content="In the aftermath of Batman's disappearance, Kate Kane must overcome her demons to protect Gotham City by donning the avatar of Batwoman",category="Movie",user=self.user_Derrick)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_title,"Batwoman")
        self.assertEquals(self.new_pitch.pitch_content,"In the aftermath of Batman's disappearance, Kate Kane must overcome her demons to protect Gotham City by donning the avatar of Batwoman")
        self.assertEquals(self.new_pitch.category,"Movie")
        self.assertEquals(self.new_pitch.user_id,self.user_Derrick.id)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        pitches = Pitch.get_pitches()
        self.assertTrue(len(pitches)==1)