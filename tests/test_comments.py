import unittest
from app.models import Comments

class CommentTest(unittest.TestCase):

    def setUp(self):
        self.new_comment = Comments(comment="Great Idea")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comments))

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comments.query.all())>0)